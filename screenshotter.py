import numpy as np
import pyautogui
import cv2
from pynput.keyboard import Key, Controller
import imutils
import os
import keyboard
from pynput import keyboard
from threading import Thread
from time import sleep

def getPet(pet):
        score = []
        pets = ['ant1', 'ant2', 'ant3', 'beaver1', 'beaver2', 'beaver3',
                'cricket1', 'cricket2', 'cricket3', 'duck1', 'duck2'
                'duck3', 'fish1', 'fish2', 'fish3', 'horse1', 'horse2', 'horse3',
                'mosquito1', 'mosquito2', 'mosquito3', 'otter1', 'otter2',
                'otter3', 'pig1', 'pig2', 'pig3']
        dir = r'pets'
        for entry in os.scandir(dir):
                if(entry.path.endswith(".png")):
                        #print(entry.path)
                        test_pet = cv2.imread(entry.path)
                        score.append(np.sum(cv2.subtract(pet, test_pet)))

        minimum = min(score)
        ind = score.index(minimum) - 1
        petID = pets[ind]
        ind
        print(score)
        return(petID)

def on_press(key, abortKey = 'esc'):
    try:
        k = key.char #single-char keys
    except:
        k = key.name # other keys

    print('pressed %s' % (k))
    if k == abortKey:
        print('end loop.....')
        return False # stop listener
    elif k == 'r':
        image = pyautogui.screenshot()

        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        cv2.imwrite("image.png", image)
        # image = imutils.resize(image, width = 600)
        # WINDOWS:
        # pet1 = image[755:1065,640:820]
        # pet2 = image[755:1065,820:1000]
        # pet3 = image[755:1065,1010:1190]

        # MAC:
        pet1 = image[955:1315,680:895]
        pet2 = image[955:1315,895:1110]
        pet3 = image[955:1315,1110:1325]

        cv2.imwrite("pet1.png", pet1)
        cv2.imwrite("pet2.png", pet2)
        cv2.imwrite("pet3.png", pet3)
        print(getPet(pet1))
        print(getPet(pet2))
        print(getPet(pet3))
    else:
        return True

def loop_fun():
    while True:
        print('sleeping')
        sleep(5)

if __name__ == '__main__':
    abortKey = 't'
    listener = keyboard.Listener(on_press = on_press, abortKey = abortKey)
    listener.start()
    listener.join()
    # start thread with loop
    #Thread(target = loop_fun, args= (), name = 'loop_func', daemon=True).start()



# def main():
#     while True:
#
#         if keyboard.is_pressed("q"):
#             break
#         elif keyboard.is_pressed("r"):
#
#
#
#             cv2.imwrite("pet1.png", pet1)
#             cv2.imwrite("pet2.png", pet2)
#             cv2.imwrite("pet3.png", pet3)
#
#         elif keyboard.is_pressed("e"):
#             getPet(pet1)
#             getPet(pet2)
#             getPet(pet3)

# TODO regex pet name from file name
#main()

# currentMouseX, currentMouseY = pyautogui.position()
# currentMouseX
# currentMouseY
# pyautogui.moveTo(635, 1060)
