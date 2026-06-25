# from datetime import datetime
# import time
# time.sleep(5)
# # c = datetime.now().today()
# # print(c)
# c = datetime.now().strftime("%A %d-%B-%Y, %H:%M:%S")
# print(c)


import pyautogui
import time
time.sleep(4)
for i in range(10):
    pyautogui.typewrite("Hello ji ", interval=0.05)

Hello ji Hello ji Hello ji Hello ji Hello ji Hello ji Hello ji Hello ji 