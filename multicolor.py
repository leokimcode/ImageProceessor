import numpy as np
from numpy import random
import matplotlib.pyplot as plt

width = 200
height = 200

array = np.zeros([height, width, 3], dtype=np.uint8)

for x in range(width):
    for y in range(height):
        array[x,y] = [random.randint(255), random.randint(255), random.randint(255)]

print(array[:width])
plt.imshow(array)
plt.show()