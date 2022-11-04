import STEP1
import numpy as np
import matplotlib.pyplot as plt

a = STEP1.meanMtrx("pins_Zendaya")
reshape = np.reshape(a,(256,256))
plt.imshow(reshape, cmap='gray')
plt.show()