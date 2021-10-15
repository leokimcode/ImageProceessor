import numpy as np
from numpy import random
import matplotlib.pyplot as plt

width = 1
height = 1

array = np.zeros([height, width, 3], dtype=np.uint8)

for x in range(width):
    for y in range(height):
        array[x,y] = [random.randint(255), random.randint(255), random.randint(255)]

plt.imshow(array)
plt.show()