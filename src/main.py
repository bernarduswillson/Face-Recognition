import STEP1
import numpy as np
import matplotlib.pyplot as plt

a = STEP1.covariance2("pins_Zendaya")
plt.imshow(a, cmap='gray')
plt.show()
