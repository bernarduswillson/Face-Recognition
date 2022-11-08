import numpy as np
import STEP1

def checkDiagonal(arr):
    print("smape check")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                continue
            else:
                if abs(arr[i][j]) > 0.001:
                    return False
    return True

def qrFactorization(arr):
    print("smape qr")
    temp = arr
    i = 0
    while(True):
        Q,R = np.linalg.qr(temp)
        temp = np.dot(R, Q)
        if(checkDiagonal(temp)):
            print("Number of Factorizations: " + str(i+1))
            break
        else:
            i += 1
        print(i)
    return temp

def printLambda(arr):
    count = 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(i == j):
                temp = arr[i][j]
                if(abs(temp) < 0.000000000001):
                    temp = 0
                print("Lamda"+str(count) +": " + str(temp))
                count += 1
    
def read():
    arr = STEP1.covariance2("tes doang")
    return arr

def main():
    arr = read()
    matrix = np.array(arr)
    print(matrix)
    printLambda(qrFactorization(arr))

if __name__ == '__main__':
    main()