import STEP1
import eigenvalue
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.time()
a = STEP1.covariance2("tes doang")
# a = [[1,1,0],[1,0,1],[0,0,1]]
a = np.array(a)
#eigenvalues = qr.qr_decomp(a)
eigenvalues = eigenvalue.carieigvals(a)
print(eigenvalues)
end=time.time()
print(end-start)
#plt.imshow(a, cmap='gray')
#plt.show()
