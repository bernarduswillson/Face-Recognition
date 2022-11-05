import cv2
import os
import numpy as np

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
        

    
def covariance1(pth):
    mean = meanMtrx(pth)
    path = r"test/" + pth
    dirs = os.listdir(path)
    c=0
    cov = [[0 for i in range(256*256)] for j in range(len(dirs))]
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        for i in range(256*256):
            cov[c][i] +=(a[i] - mean[i])
        c+=1
    return cov

def transpose(mtrx):
    result = [[mtrx[j][i] for j in range(len(mtrx))] for i in range(len(mtrx[0]))]
    return result

def matrixmult(a,b):
    result = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                print(i,j,k)
                result[i][j] += a[i][k] * b[k][j]
    return result

def covariance2(pth):
    cov = covariance1(pth)
    covT = np.transpose(cov)
    result = np.matmul(cov,covT)
    return result

