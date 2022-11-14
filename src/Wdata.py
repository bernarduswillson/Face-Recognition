import STEP1
import eigenvalue
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.time()
def ImgToMtrx(img):
    image = cv2.imread(r"test/" + img)
    image = cv2.resize(image,(256,256), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def meanMtrx(pth):
    mean = [[0 for i in range(256)] for j in range(256)]
    c=0
    path = r"test/" + pth
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
    path = r"test/" + pth
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

a = STEP1.covariance2("DATASET")
normalized_mat = STEP1.covariance1("DATASET")
covT = np.transpose(normalized_mat)
eigenvalues, eigenvectors = eigenvalue.carieigvals(a)
eigenface = np.matmul(covT,eigenvectors)
eigenface = np.transpose(eigenface)
a = 0
resultarr=[]
for i in range(5):
    eigenfaces=eigenface[i]
    result=[[0 for i in range(256)] for j in range(256)]
    for i in range (256):
        for j in range (256) :
            result[i][j]+=eigenfaces[a]
            a +=1
    a=0
    resultarr.append(result)

def totaleigenface(resultarr):
    mateigen = [[0 for i in range(256)] for j in range(256)]
    for i in range(5):
        mateigen = np.add(mateigen,resultarr[i])
    return mateigen

def W(resultarr,pth):
    wtotal=[]
    W = [[0 for i in range(256)] for j in range(256)]
    path = r"test/" + pth
    a = normalized(pth)
    dirs = os.listdir(path)
    for i in range(len(dirs)):
        W[i] = np.matmul(a[i],totaleigenface(resultarr))
        wtotal.append(W[i])
    return wtotal

a = W(resultarr,"DATASET")

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

b = WTes(resultarr,"DATASET","Selena Gomez191_4391.jpg")

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

z,ii = EuclideanDistance(a,b)
print(z,ii)
print("---------------------------------------")
path = r"test/" + "DATASET"
dirs = os.listdir(path)
k = 0
for file in dirs:
    if (k==ii):
        print(ii)
        print(z)
        print(file)
    k+=1