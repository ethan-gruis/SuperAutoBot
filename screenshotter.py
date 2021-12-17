import numpy as np
import pyautogui
import cv2
from pynput.keyboard import Key, Controller
import imutils
import time
import os


image = pyautogui.screenshot()

image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

cv2.imwrite("image.png", image)
# image = imutils.resize(image, width = 600)
pet1 = image[755:1065,640:820]
pet2 = image[755:1065,820:1000]
pet3 = image[755:1065,1010:1190]


cv2.imwrite("pet1.png", pet1)
cv2.imwrite("pet2.png", pet2)
cv2.imwrite("pet3.png", pet3)

def getPet(pet):
        score = []
        pets = ['ant1', 'ant2', 'ant3', 'beaver1', 'beaver2', 'beaver3',
                'cricket1', 'cricket2', 'cricket3', 'duck1', 'duck2'
                'duck3', 'fish1', 'fish2', 'fish3', 'horse1', 'horse2', 'horse3',
                'mosquito1', 'mosquito2', 'mosquito3', 'otter1', 'otter2',
                'otter3', 'pig1', 'pig2', 'pig3']
        dir = r'C:\Users\egruis\Documents\Projects\SuperAutoPetsBot\pets'
        for entry in os.scandir(dir):
                if(entry.path.endswith(".png")):
                        #print(entry.path)
                        test_pet = cv2.imread(entry.path)
                        score.append(np.sum(cv2.subtract(pet3, test_pet)))

        minimum = min(score)
        ind = score.index(minimum) - 1
        petID = pets[ind]
        ind
        print(score)
        return(petID)

# TODO regex pet name from file name
getPet(pet1)
getPet(pet2)
getPet(pet3)

# currentMouseX, currentMouseY = pyautogui.position()
# currentMouseX
# currentMouseY
# pyautogui.moveTo(635, 1060)
