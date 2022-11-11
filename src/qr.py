import numpy as np

def qr_decomp(A) :
    m, n = A.shape
    Q = np.zeros((m,n))
    for i, column in enumerate(A.T) :
            Q[:,i] = column

            for prev in Q.T[:i] :
                Q[:,i] -= np.dot(prev, column) / np.dot(prev, prev) * prev

    Q /= np.linalg.norm(Q,axis=0)
    R = np.dot(Q.T, A)


    return Q, R

def QR_Decomposition(A):
    n, m = A.shape # get the shape of A

    Q = np.empty((n, n)) # initialize matrix Q
    u = np.empty((n, n)) # initialize matrix u

    u[:, 0] = A[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])

    for i in range(1, n):

        u[:, i] = A[:, i]
        for j in range(i):
            u[:, i] -= (A[:, i] @ Q[:, j]) * Q[:, j] # get each u vector

        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i]) # compute each e vetor

    R = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):
            R[i, j] = A[:, j] @ Q[:, i]

    return Q, R