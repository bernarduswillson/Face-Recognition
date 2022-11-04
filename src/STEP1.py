import cv2
import os

def ImgToMtrx(img):
    image = cv2.imread(r"test/" + img)
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    return result

def meanMtrx(pth):
    mean = [0 for i in range(256*256)]
    c=0
    path = r"test/" + pth
    dirs = os.listdir(path)
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        c+=1
        for i in range(256*256):
            mean[i] += a[i]
    for i in range(256*256):
        mean[i] /= c
    return mean
        

    