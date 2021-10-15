import numpy as np
import matplotlib.pyplot as plt

np.array([[(0.5, 0.5, 0.5)]]).shape
#MxNx3 (3 is RGB)
#MxN is grayscale
#MxNx4 (4 RGBA)
(2, 2, 3)

r = 235
g = 64
b = 52

#format in RGB
plt.imshow([[(r / 255, g / 255, b / 255)]])
plt.show()