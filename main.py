import sys
from os import startfile
from time import sleep

import pyautogui
import pydirectinput
from psutil import process_iter


if __name__ == '__main__':
    kkrieger = sys.argv[1]
    address = sys.argv[3]
    startfile(kkrieger)
    sleep(14)
    screen1 = pyautogui.screenshot()
    screen1.save(address+'screen1.png')
    pydirectinput.press('f11')
    pydirectinput.press('enter', presses=2)
    pydirectinput.keyDown('w')
    sleep(12)
    pydirectinput.press('f11')
    screen2 = pyautogui.screenshot()
    sleep(1)
    for proc in process_iter():
        if proc.name() == 'pno0001.exe':
            proc.kill()
    screen2.save(address+'screen2.png')
