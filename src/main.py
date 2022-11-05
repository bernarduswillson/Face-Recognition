import STEP1
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.time()
a = STEP1.covariance2("pins_Alexandra Daddario")
end=time.time()
print(end-start)
plt.imshow(a, cmap='gray')
plt.show()
