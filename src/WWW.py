import STEP1
import eigenvalue
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import time


def ImgToMtrx(img):
    image = cv2.imread(r"" + img)
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def meanMtrx(pth):
    mean = [[0 for i in range(256)] for j in range(256)]
    c=0
    path = r"" + pth
    dirs = os.listdir(path)
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        c+=1
        for i in range(256):
            for j in range(256):
                mean[i][j] += a[i][j]
    for i in range(256):
        for j in range(256):
            mean[i][j] /= c
    return mean

def normalized(pth):
    mean = meanMtrx(pth)
    path = r"" + pth
    dirs = os.listdir(path)
    k=0
    norm = [[[0 for i in range(256)] for j in range(256)] for k in range(len(dirs))]
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        for i in range(256):
            for j in range(256):
                norm[k][i][j] +=(a[i][j] - mean[i][j])
        k+=1
    return norm

def totaleigenface(resultarr):
    mateigen = [[0 for i in range(256)] for j in range(256)]
    for i in range(5):
        mateigen = np.add(mateigen,resultarr[i])
    return mateigen

def W(resultarr,pth):
    wtotal=[]
    W = [[0 for i in range(256)] for j in range(256)]
    path = r"" + pth
    a = normalized(pth)
    dirs = os.listdir(path)
    for i in range(len(dirs)):
        W[i] = np.matmul(a[i],totaleigenface(resultarr))
        wtotal.append(W[i])
    return wtotal

def normalizedT(pthdata,pth):
    mean = meanMtrx(pthdata)
    norm = [[0 for i in range(256)] for j in range(256)]
    a = ImgToMtrx(pth)
    for i in range(256):
        for j in range(256):
            norm[i][j] +=(a[i][j] - mean[i][j])
    return norm

def WTes(resultarr,pthdata,pth):
    W = [[0 for i in range(256)] for j in range(256)]
    a = normalizedT(pthdata,pth)
    W = np.matmul(a,totaleigenface(resultarr))
    return W

def EuclideanDistance(a,b):
    min = 9999999999999999999
    selisih = [0 for i in range(len(a))]
    for i in range(len(a)):
        selisih[i] = np.subtract(b,a[i])
        selisih[i] = np.square(selisih[i])
        selisih[i] = np.sum(selisih[i])
        selisih[i] = np.sqrt(selisih[i])
        if (min>selisih[i]):
            min = selisih[i]
            index = i
    return min, index