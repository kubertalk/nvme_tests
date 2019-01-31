#!/bin/python
import os
import time
import run_nvme_test
print("this is nvme boot")

while_count = 0
while True:
    val=os.system("ls /dev/nvme0n1")
    if val > 0:
        while_count +=1
        if while_count % 100 ==0:
            print("nvme device isn't ready.")
    else:
        break
    time.sleep(3)
                                        
print("start nvme host test")
run_nvme_test.main()
