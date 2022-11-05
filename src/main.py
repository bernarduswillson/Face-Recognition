import STEP1
import eigenvalue
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.time()
a = STEP1.covariance2("pins_Alexandra Daddario")
# a = [[3,-2,0],[-2,3,0],[0,0,5]]
eigenvalues = eigenvalue.find_eigenvalues(a)
print(eigenvalues)
end=time.time()
print(end-start)
#plt.imshow(a, cmap='gray')
#plt.show()
