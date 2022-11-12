import STEP1
import eigenvalue
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.time()
norm=STEP1.covariance1("data")
# a = np.cov(STEP1.covariance1("pins_Alexandra Daddario"))
# a = STEP1.covariance2("data")
# a = [[1,1,0],[1,0,1],[0,0,1]]
# a = np.array(a)
#eigenvalues = qr.qr_decomp(a)
# eigenvalues,eigvec = eigenvalue.carieigvals(a)
# eigenvalues,eigvec = np.linalg.eig(a)
# face=eigenvalue.eigenfacefromeigvec(eigvec)
# print(eigenvalues)
a=[[0 for i in range(256)] for j in range(256)]
for i in range(len(norm)):
    for j in range(256):
        for k in range(256):
            a[j][k] = norm[i][j*256+k]
    plt.imshow(a, cmap='gray')
    plt.show()
# eigval,eigvector=eigenvalue.carieigvals(a)
# end=time.time()
# print(eigvector)
# print(end-start)
# plt.imshow(eigvector, cmap='gray')
# plt.show()

