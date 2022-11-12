import STEP1
import eigenvalue
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.time()
a = STEP1.covariance2("pins_Alexandra Daddario")
#a = [[1,1,0],[1,0,1],[0,0,1]]
#a = np.array(a)
#eigenvalues = qr.qr_decomp(a)
normalized_mat = STEP1.covariance1("pins_Alexandra Daddario")
covT = np.transpose(normalized_mat)
#shapess = covT.shape
#print (shapess)
eigenvalues, eigenvectors = eigenvalue.carieigvals(a)
eigenface = np.matmul(covT,eigenvectors)
eigenface = np.transpose(eigenface)
a = 0
# eigenfaces = eigenface[0]#ini baru face 0 nya doang
# result1 = [[0 for i in range(256)] for j in range(256)]
# for i in range (256):
#     for j in range (256) :
#         result1[i][j]+=eigenfaces[a]
#         a +=1
# a = 0
# eigenfaces = eigenface[1]#ini baru face 0 nya doang
# result2 = [[0 for i in range(256)] for j in range(256)]
# for i in range (256):
#     for j in range (256) :
#         result2[i][j]+=eigenfaces[a]
#         a +=1
# a = 0
# eigenfaces = eigenface[2]#ini baru face 0 nya doang
# result3 = [[0 for i in range(256)] for j in range(256)]
# for i in range (256):
#     for j in range (256) :
#         result3[i][j]+=eigenfaces[a]
#         a +=1
# a = 0
# eigenfaces = eigenface[3]#ini baru face 0 nya doang
# result4 = [[0 for i in range(256)] for j in range(256)]
# for i in range (256):
#     for j in range (256) :
#         result4[i][j]+=eigenfaces[a]
#         a +=1

resultarr=[]
for i in range(len(eigenface)):
    eigenfaces=eigenface[i]
    result=[[0 for i in range(256)] for j in range(256)]
    for i in range (256):
        for j in range (256) :
            result[i][j]+=eigenfaces[a]
            a +=1
    a=0
    resultarr.append(result)
#eigenfaces = np.array(eigenface)
#eigenfaces = eigenface[0]
#aa = eigenvectors.shape
#print(aa)
#print(eigenvectors[0])
# result1 = np.array(result1)
# #result1 = np.mul(eigenvectors[0][0],result1)
# result2 = np.array(result2)
# #result2 = np.mul(eigenvectors[0][1],result2)
# result3 = np.array(result3)
# #result3 = np.mul(eigenvectors[0][2],result3)
# result4 = np.array(result4)
#result4 = np.mul(eigenvectors[0][3],result1)
"""result = [[0 for i in range(256)] for j in range(256)]
for i in range (256):
    for j in range (256) :
        result[i][j]+=result1[i][j] + result2[i][j] + result3[i][j] + result4[i][j]"""
# print(result1)
# print(result2)
# print(result3)
# print(result4)
#reshape1 = np.reshape(eigenface,(256,256))
#print(eigenface)
#m,n = eigenface.shape
#print(m,n)
end=time.time()
print(end-start)
# plt.imshow(result1, cmap='gray')
# plt.show()
# plt.imshow(result2, cmap='gray')
# plt.show()
# plt.imshow(result3, cmap='gray')
# plt.show()
# plt.imshow(result4, cmap='gray')
# plt.show()
for i in range(len(resultarr)):
    plt.imshow(resultarr[i], cmap='gray')
    plt.show()