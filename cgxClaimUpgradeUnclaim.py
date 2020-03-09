#!/usr/bin/env python3
import cgxinit
import cloudgenix
import sys
import csv
import myCGX
import time


# create CGX object and authenticate
cgx, args = cgxinit.go()
myCGX.initmyCGX(cgx)


# open csv file
with open(args["csv_file"]) as cvs_file:
    cvs_reader = csv.reader(cvs_file, delimiter=',')
    # skip header
    next(cvs_reader)

    devices = {}
    for row in cvs_reader:
        if not len(row) == 2:
            continue
        devices[row[0]] = {}
        devices[row[0]]["target"] = row[1]
        devices[row[0]]["m_id"] = myCGX.getMachineID(row[0])
        devices[row[0]]["state"] = "start"
        devices[row[0]]["i_id"] = myCGX.getImageByName(row[1])

    # loop through states
    seconds = 0
    while True:
        print("--- Timer {0} seconds".format(seconds))
        done = True
        for serial, device in devices.items():
            if device["state"] == "start":
                done = False
                device["state"] = "wait_online"
                print("Waiting for {serial} to be online".format(
                    serial=serial))
            elif device["state"] == "wait_online":
                done = False
                machine = cgx.get.machines(machine_id=device["m_id"])
                if not machine:
                    print("Error in getting {serial} status. Error {err}".format(
                        serial=serial, err=machine.cgx_content))
                    sys.exit(1)
                machine = machine.cgx_content
                if machine["connected"]:
                    print("Machine {serial} is online".format(serial=serial))
                    if machine["machine_state"] == "claimed":
                        device["e_id"] = machine["em_element_id"]
                        print("Machine {serial} is claimed".format(
                            serial=serial))
                        device["state"] = "claimed"
                    else:
                        print("Claiming machine {serial}".format(
                            serial=serial))
                        device["state"] = "claiming"
                        claim = cgx.post.tenant_machine_operations(
                            device["m_id"], '{"inventory_op":"claim"}')
                        if not claim:
                            print("Error in claiming {serial}. Reason {r}".format(
                                serial=serial, r=machine.cgx_content))
                            sys.exit(1)
                else:
                        print("Waiting for {serial} to be online".format(
                            serial=serial))
            elif device["state"] == "claiming":
                done = False
                machine = cgx.get.machines(machine_id=device["m_id"])
                if not machine:
                    print("Error in getting {serial} status. Error {err}".format(
                        serial=serial, err=machine.cgx_content))
                    sys.exit(1)
                machine = machine.cgx_content
                if machine["connected"]:
                    if machine["machine_state"] == "claimed":
                        print("Machine {serial} is claimed".format(
                            serial=serial))
                        device["state"] = "claimed"
                        device["e_id"] = machine["em_element_id"]
                        element = cgx.get.elements(element_id=device["e_id"])
                        if not element.cgx_status:
                            print("Error in getting {serial} element {eid}. Error {err}".format(
                                serial=serial, err=machine.cgx_content, eid=device["e_id"]))
                            sys.exit(1)
                        element = element.cgx_content
                        if element["state"] in["ready", "bound"] and element["connected"]:
                            print("Machine {serial} is claimed. Element id {eid}".format(
                                serial=serial, eid=device["e_id"]))
                            device["state"] = "claimed"
                        else:
                            print("Waiting for {serial} to be claimed and online".format(
                                serial=serial))
                    else:
                        print("Waiting for {serial} to be claimed and online".format(
                            serial=serial))
            elif device["state"] == "claimed":
                done = False

                element_id = device["e_id"]
                state = cgx.get.software_status(element_id)
                if not state.cgx_status:
                    ValueError(
                        "Can't Get software status for element %s: %s", element_id, state.cgx_content)
                state = state.cgx_content["items"][0]
                if state["active_version"] == device["target"]:
                    print("No need to upgrade {serial}".format(serial=serial))
                    if args["noUnclaim"] :
                        device["state"] = "done"
                    else:
                        device["state"] = "unclaim"
                else:
                    print("Upgrading {serial}".format(serial=serial))
                    state = cgx.get.state(element_id).cgx_content
                    new_state = {}
                    new_state['_schema'] = state['_schema']
                    new_state['_etag'] = state['_etag']
                    new_state['id'] = state['id']
                    new_state['scheduled_upgrade'] = state['scheduled_upgrade']
                    new_state['image_id'] = device["i_id"]
                    out = cgx.put.state(element_id, new_state)
                    if not out.cgx_status:
                        ValueError("Unable to upgrade ION: %s", out.cgx_content)
                    device["state"] = "upgrading"
            elif device["state"] == "upgrading":
                done = False
                target_version = device["target"]
                element_id = device["e_id"]
                # first the upgrade state needs not to be None to start the upgrade
                # then it needs to be None to complete the upgrade
                out = cgx.get.software_status(element_id)
                if out.cgx_content["items"][0]['active_version'] != target_version:
                    print("Waiting for {serial} to be upgraded".format(
                        serial=serial))
                else:
                    print("{serial} is upgraded".format(serial=serial))
                    if args["noUnclaim"] :
                        device["state"] = "done"
                    else:
                        device["state"] = "unclaim"
            elif device["state"] == "unclaim":
                done = False
                print("Unclaiming {serial}".format(serial=serial))
                data = {"action": "declaim", "parameters": None}
                res = cgx.post.tenant_element_operations(device["e_id"], data)
                if not res.cgx_status:
                    ValueError("Unable to unclaim ION: %s", res.cgx_content)
                device["state"] = "waiting_after_unclaim"
            elif device["state"] == "waiting_after_unclaim":
                machine = cgx.get.machines(machine_id=device["m_id"])
                if not machine:
                    print("Error in getting {serial} status. Error {err}".format(serial=serial, err=machine.cgx_content))
                    sys.exit(1)
                machine=machine.cgx_content
                if machine["connected"]:
                    print("{serial} is ready".format(serial=serial))
                else:
                    print("{serial} is waiting to become online after unclaim".format(serial=serial))
                    done = False
            elif device["state"] == "done":
                print("{serial} is ready".format(serial=serial))
        time.sleep(10)
        if done:
            break
        seconds += 10

