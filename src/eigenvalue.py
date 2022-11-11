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

def QR_eigvals(A, tol=1e-12, maxiter=1000):
    "Find the eigenvalues of A using QR decomposition."

    A_old = np.copy(A)
    A_new = np.copy(A)

    diff = np.inf
    i = 0
    while (diff > tol) and (i < maxiter):
        A_old[:, :] = A_new
        Q, R = qr.QR_Decomposition(A_old)

        A_new[:, :] = R @ Q
        
        diff = np.abs(A_new - A_old).max()
        i += 1

    eigvals = np.diag(A_new)

    return eigvals