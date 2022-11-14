import DataCov
import Eigen
import numpy as np

def EigenFace(pth):
    cov = DataCov.covariance(pth)
    norm = DataCov.normalized(pth)
    normT = np.transpose(norm)
    EigenVal, EigenVec = Eigen.EigenV(cov)
    EigenFace = np.matmul(normT,EigenVec)
    EigenFace = np.transpose(EigenFace)
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
