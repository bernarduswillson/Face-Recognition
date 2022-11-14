import STEP1
import eigenvalue
import numpy as np

a = STEP1.covariance2("DATASET")
normalized_mat = STEP1.covariance1("DATASET")
covT = np.transpose(normalized_mat)
test=STEP1.ImgToMtrx("data/B94A01FC-8B25-4CEE-AB70-42AC0E0BF03C.jpg")
test=np.array(test)
test=test.flatten()
normtest=test-STEP1.meanMtrx("DATASET")
eigenvalues, eigenvectors = eigenvalue.carieigvals(a)
eigenface = np.matmul(covT,eigenvectors)
eigenface = np.transpose(eigenface)
a = 0
resultarr=[]
for i in range(10):
    eigenfaces=eigenface[i]
    result=[[0 for i in range(256)] for j in range(256)]
    for i in range (256):
        for j in range (256) :
            result[i][j]+=eigenfaces[a]
            a +=1
    a=0
    resultarr.append(result)