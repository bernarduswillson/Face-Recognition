import cv2
import os
import numpy as np

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

def normalizedD(pth):
    mean = meanMtrx(pth)
    path = r"" + pth
    dirs = os.listdir(path)
    k = 0
    norm = [[[0 for i in range(256)] for j in range(256)] for k in range(len(dirs))]
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        for i in range(256):
            for j in range(256):
                norm[k][i][j] +=(a[i][j] - mean[i][j])
        k += 1
    return norm

def EFSum(EFMatrix):
    EFMatSum = [[0 for i in range(256)] for j in range(256)]
    for i in range(len(EFMatrix)):
        EFMatSum = np.add(EFMatSum, EFMatrix[i])
    return EFMatSum

def WData(EFMatrix, pth):
    WTotal = []
    W = [[0 for i in range(256)] for j in range(256)]
    path = r"" + pth
    norm = normalizedD(pth)
    dirs = os.listdir(path)
    for i in range(len(dirs)):
        W[i] = np.matmul(norm[i], EFSum(EFMatrix))
        WTotal.append(W[i])
    return WTotal

def normalizedT(pthdata, pth):
    mean = meanMtrx(pthdata)
    norm = [[0 for i in range(256)] for j in range(256)]
    a = ImgToMtrx(pth)
    for i in range(256):
        for j in range(256):
            norm[i][j] += (a[i][j] - mean[i][j])
    return norm

def WTest(EFMatrix, pthdata, pth):
    W = [[0 for i in range(256)] for j in range(256)]
    norm = normalizedT(pthdata, pth)
    W = np.matmul(norm, EFSum(EFMatrix))
    return W

def MinEuclideanDistance(WData,WTest):
    min = 9999999999999999999
    selisih = [0 for i in range(len(WData))]
    t=0
    max=0
    for i in range(len(WData)):
        selisih[i] = np.subtract(WData[i],WTest)
        selisih[i] = np.square(selisih[i])
        selisih[i] = np.sum(selisih[i])
        selisih[i] = np.sqrt(selisih[i])
        if (max<selisih[i]):
            max = selisih[i]
        if (min > selisih[i]):
            min = selisih[i]
            index = i
    return min, index, max
