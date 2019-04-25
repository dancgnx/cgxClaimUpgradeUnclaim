#Upgrade CGX devices in bulk.

Instructions:

* Install python3
* Install cloudgenix python sdk : pip3 install cloudgenix
* Setup authentication as listed below
* Create a csv file with the example at devicelist.csv
* run the script using: python3 cgxClaimUpgradeUnclaim.py --csv CSV_FILENAME 

cgxClaimUpgradeUnclaim.py looks for the following for AUTH, in this order of precedence:

* --email or --password options on the command line.
* CLOUDGENIX_USER and CLOUDGENIX_PASSWORD values imported from cloudgenix_settings.py
* CLOUDGENIX_AUTH_TOKEN value imported from cloudgenix_settings.py
* X_AUTH_TOKEN environment variable
* AUTH_TOKEN environment variable
* Interactive prompt for user/pass (if one is set, or all other methods fail.)


Example of a run:
```
bash$ python3 ./cgxClaimUpgradeUnclaim.py --csv devicelist.csv 
--- Timer 0 seconds
Waiting for 20-001014-3515 to be online
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be online
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be online
--- Timer 10 seconds
Waiting for 20-001014-3515 to be online
Machine 564d187a-9700-120d-46b3-764e7628a64d is online
Claiming machine 564d187a-9700-120d-46b3-764e7628a64d
Machine 564d9474-5195-1a32-b436-6f1961c91847 is online
Claiming machine 564d9474-5195-1a32-b436-6f1961c91847
--- Timer 20 seconds
Machine 20-001014-3515 is online
Claiming machine 20-001014-3515
Machine 564d187a-9700-120d-46b3-764e7628a64d is claimed
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be claimed and online
Machine 564d9474-5195-1a32-b436-6f1961c91847 is claimed
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be claimed and online
--- Timer 30 seconds
Waiting for 20-001014-3515 to be claimed and online
Upgrading 564d187a-9700-120d-46b3-764e7628a64d
Upgrading 564d9474-5195-1a32-b436-6f1961c91847
--- Timer 40 seconds
Waiting for 20-001014-3515 to be claimed and online
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 50 seconds
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 60 seconds
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 70 seconds
Machine 20-001014-3515 is claimed
Machine 20-001014-3515 is claimed. Element id 15562317222060185
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 80 seconds
Upgrading 20-001014-3515
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 90 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 100 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 110 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 120 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 130 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 140 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 150 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Waiting for 564d9474-5195-1a32-b436-6f1961c91847 to be upgraded
--- Timer 160 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
564d9474-5195-1a32-b436-6f1961c91847 is upgraded
--- Timer 170 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
Unclaiming 564d9474-5195-1a32-b436-6f1961c91847
--- Timer 180 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 190 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 200 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 210 seconds
Waiting for 20-001014-3515 to be upgraded
Waiting for 564d187a-9700-120d-46b3-764e7628a64d to be upgraded
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 220 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is upgraded
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 230 seconds
Waiting for 20-001014-3515 to be upgraded
Unclaiming 564d187a-9700-120d-46b3-764e7628a64d
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 240 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is waiting to become online after unclaim
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 250 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is waiting to become online after unclaim
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 260 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is waiting to become online after unclaim
564d9474-5195-1a32-b436-6f1961c91847 is waiting to become online after unclaim
--- Timer 270 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is waiting to become online after unclaim
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 280 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is waiting to become online after unclaim
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 290 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is waiting to become online after unclaim
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 300 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is waiting to become online after unclaim
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 310 seconds
Waiting for 20-001014-3515 to be upgraded
564d187a-9700-120d-46b3-764e7628a64d is waiting to become online after unclaim
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 320 seconds
20-001014-3515 is upgraded
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 330 seconds
Unclaiming 20-001014-3515
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 340 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 350 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 360 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 370 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 380 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 390 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 400 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 410 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 420 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 430 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 440 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 450 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 460 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 470 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 480 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 490 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 500 seconds
20-001014-3515 is waiting to become online after unclaim
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
--- Timer 510 seconds
20-001014-3515 is ready
564d187a-9700-120d-46b3-764e7628a64d is ready
564d9474-5195-1a32-b436-6f1961c91847 is ready
```