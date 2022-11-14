import numpy as np

def QR_Decomposition(cov):
    N, M = cov.shape
    Q = np.empty((N, N))
    u = np.empty((N, N))
    u[:, 0] = cov[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])
    for i in range(1, N):
        u[:, i] = cov[:, i]
        for j in range(i):
            u[:, i] -= (cov[:, i] @ Q[:, j]) * Q[:, j]
        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i])
    R = np.zeros((N, M))
    for i in range(N):
        for j in range(i, M):
            R[i, j] = cov[:, j] @ Q[:, i]
    return Q, R

def EigenV(cov):
    pQ = np.eye(cov.shape[0])
    for i in range(100):
        Q,R = np.linalg.qr(cov)
        pQ = pQ @ Q
        cov = R @ Q
    return np.diag(cov), pQ

