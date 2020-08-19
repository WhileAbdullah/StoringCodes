import pyautogui
from PIL import Image,ImageGrab
#import numpy as array
import time

def hit(key):
    pyautogui.keyDown(key)


def isColide(data):
    for i in range(300,415):
         for j in range(600,650):
            if data[i,j]>100:
                return True
    return False



if __name__ == "__main__":
    print("Hey...Dinasaur game is about to start in 3 seconds.")
    time.sleep(3)
    hit('up')

    while True:
        image= ImageGrab.grab().convert('L')
        data=image.load()
        image.show()
        if isColide(data):
            hit('up')

        