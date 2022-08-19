from fps_inspector_sdk import fps_inspector
import matplotlib
import matplotlib.pyplot as plt
import time
from os import startfile
from time import sleep
import os

import numpy
import pyautogui
from psutil import process_iter
import pydirectinput

matplotlib.use('Agg')


def main():
    def float_formatter(x): return "%.5f" % x
    numpy.set_printoptions(
        formatter={'float_kind': float_formatter}, threshold=numpy.inf)
    pid = os.getpid()
    fps_inspector.start_fliprate_recording(pid)
    time.sleep(10)
    fps_inspector.stop_fliprate_recording()
    data = fps_inspector.get_all_fliprates()
    print(data)
    plt.figure()
    data[data.ScreenTime != 0][['FPS', 'FlipRate', 'ScreenTime']].plot(
        x='ScreenTime', subplots=True)
    plt.savefig('plot.png')
    data.to_csv('scores.csv')
    plt.close()


if __name__ == "__main__":
    startfile('pno0001.exe')
    sleep(15)
    pydirectinput.press('f11')
    screen = pyautogui.screenshot('screenshot.png')
    sleep(30)
    pydirectinput.press('enter', presses=2)
    pydirectinput.keyDown('w')
    pydirectinput.press('f11')
    sleep(20)
    screen = pyautogui.screenshot('screenshot1.png')
    for proc in process_iter():
        if proc.name() == 'pno0001.exe':
            proc.kill()
