import pyautogui
import time

time.sleep(2)

msg = input("Type the msg: ")
n = int(input("How many times? -> "))

for i in range(n):
    pyautogui.write(msg)
    time.sleep(0.5)
    pyautogui.press("Enter")
