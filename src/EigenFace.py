import DataCov
import Eigen
import numpy as np
import matplotlib.pyplot as plt

def EigenFace(pth):
    cov = DataCov.covariance(pth)
    norm = DataCov.normalized(pth)
    EigenVal, EigenVec = Eigen.EigenV(cov)
    EigenFace = np.matmul(EigenVec,norm)
    k = 0
    resultarr = []
    leneigen = round(len(norm)*0.06)
    for i in range(leneigen):
        EigenFaces = EigenFace[i]
        result=[[0 for i in range(256)] for j in range(256)]
        for i in range (256):
            for j in range (256) :
                result[i][j] += EigenFaces[k]
                k += 1
        k = 0
        resultarr.append(result)
    return resultarr