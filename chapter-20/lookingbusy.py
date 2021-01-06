import pyautogui
import time
while True:
   pyautogui.move(0.3, 0, duration=0.25)
   time.sleep(60)
   pyautogui.move(0, 0.3, duration=0.25)
   time.sleep(60)
   pyautogui.move(-0.3, 0, duration=0.25)
   time.sleep(60)
   pyautogui.move(0, -0.3, duration=0.25)
   time.sleep(60)