import numpy as np
import qr


def diag_sign(matrix) :
    D = np.diag(np.sign(np.diag(matrix)))
    return D

def adjust_sign(Q,R):
    D = diag_sign(Q)
    Q[:, :] = np.dot(Q, D)
    R[:, :] = np.dot(D, R)

    return Q, R

def carieigvals(a) :
    for i in range(100) :
        q, r = qr.qr_decomp(a)
        a = np.dot(r, q)
    return np.diag(a)   