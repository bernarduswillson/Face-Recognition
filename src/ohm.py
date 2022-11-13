import cv2
import os
import numpy as np

def ohm(eigenface,normimg):
    ohmarr=[]
    normimgmat=[[0 for i in range(256*256)] for j in range(1)]
    for i in range(256*256):
        normimgmat[0][i]=normimg[i]

    for i in range (len(eigenface)):
        neweigf=eigenface[i]
        neweigf=np.array(neweigf)
        neweigf=neweigf.flatten()
        normimgmat=np.array(normimgmat)
        val=np.matmul(normimgmat,neweigf)
        ohmarr.append(val)
    return ohmarr

def distance(newohm):
    distttt=0
    for i in range(len(newohm)):
        distttt+=newohm[i][0]**2
    finaldist=np.sqrt(distttt)
    return finaldist