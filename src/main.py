import time
import EigenFace
import Euclidian
import os

dataset = input("input dataset path: ")
test = input("input test image path: ")

start=time.time()
EigenFace = EigenFace.EigenFace(dataset)
WData = Euclidian.WData(EigenFace, dataset)
WTest = Euclidian.WTest(EigenFace, dataset, test)
val, index = Euclidian.MinEuclideanDistance(WData,WTest)
print(val, index)
print("---------------------------------------")
path = r"" + dataset
dirs = os.listdir(path)
k = 0
for file in dirs:
    if (k==index):
        print(index)
        print(val)
        print(file)
    k += 1
end = time.time()
print(end-start)