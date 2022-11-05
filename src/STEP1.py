import cv2
import os

def ImgToMtrx(img):
    image = cv2.imread(r"test/" + img)
    image = cv2.resize(image,(64,64), interpolation = cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = gray_image.flatten()
    return result

def meanMtrx(pth):
    mean = [0 for i in range(64*64)]
    c=0
    path = r"test/" + pth
    dirs = os.listdir(path)
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        c+=1
        for i in range(64*64):
            mean[i] += a[i]
    for i in range(64*64):
        mean[i] /= c
    return mean
        

    
def covariance1(pth):
    mean = meanMtrx(pth)
    path = r"test/" + pth
    dirs = os.listdir(path)
    c=0
    cov = [[0 for i in range(64*64)] for j in range(len(dirs))]
    for file in dirs:
        a = ImgToMtrx(pth+"/"+file)
        for i in range(64*64):
            print("cov[",c,"][",i,"]")
            cov[c][i] +=(a[i] - mean[i])
        c+=1
    return cov

def transpose(mtrx):
    result = [[mtrx[j][i] for j in range(len(mtrx))] for i in range(len(mtrx[0]))]
    return result

def matrixmult(a,b):
    print(1)
    result = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    print(2)
    for i in range(len(a)):
        print(3)
        for j in range(len(b[0])):
            print(4)
            for k in range(len(b)):
                print(i,j,k)
                result[i][j] += a[i][k] * b[k][j]
    return result

def covariance2(pth):
    print(1)
    cov = covariance1(pth)
    print(2)
    covT = transpose(cov)
    print(3)
    result = matrixmult(cov,covT)
    print(4)
    return result

