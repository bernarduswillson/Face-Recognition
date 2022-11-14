import STEP1
import eigenvalue
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import time
import W


datset=input("input dataset path: ")
tes=input("input test image path: ")
start=time.time()
a = STEP1.covariance2(datset)
normalized_mat = STEP1.covariance1(datset)
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

a = W.W(resultarr,datset)
b = W.WTes(resultarr,datset,tes)
z,ii = W.EuclideanDistance(a,b)
print(z,ii)
threshold=750000000
kemiripan=((threshold-z)/threshold)*100
print("---------------------------------------")



path = r"" + datset
dirs = os.listdir(path)
k = 0
for file in dirs:
    if (k==ii):
        print(ii)
        print(z)
        print("kemiripan: ",kemiripan,"%")
        print(file)
    k+=1

end=time.time()
print(end-start)