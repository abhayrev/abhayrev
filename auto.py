import pyautogui
import time
time.sleep(3)
count=0
while count<10:
  pyautogui.typewrite("hello")
  pyautogui.press("enter")
  count=count+1
