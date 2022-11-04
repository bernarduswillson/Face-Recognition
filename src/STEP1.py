import cv2
import os

def ImgToMtrx(img):
    image = cv2.imread(r"src/" + img)
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    return result

def readFolder():
    path = r"src"
    dirs = os.listdir(path)
    for file in dirs:
        print(file)

