import cv2
import os
import numpy as np

def ImgToMtrx(img):
    image = cv2.imread(r"" + img)
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    return result

def meanMtrx(pth):
    mean = [0 for i in range(256*256)]
    c = 0 
    dirs = os.listdir(r"" + pth)
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        c+=1
        for i in range(256*256):
            mean[i] += a[i]
    for i in range(256*256):
        mean[i] /= c
    return mean
    
def normalized(pth):
    mean = meanMtrx(pth)
    dirs = os.listdir(r"" + pth)
    c = 0
    norm = [[0 for i in range(256*256)] for j in range(len(dirs))]
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        for i in range(256*256):
            norm[c][i] += (a[i] - mean[i])
        c += 1
    return norm

def covariance(pth):
    norm = normalized(pth)
    normT = np.transpose(norm)
    cov = np.matmul(norm,normT)
    return cov