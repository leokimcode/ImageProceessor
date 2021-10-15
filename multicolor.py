import numpy as np
from numpy import random
import matplotlib.pyplot as plt

width = 200
height = 200

array = np.zeros([height, width, 3], dtype=np.uint8)

for x in range(width):
    for y in range(height):
        r = random.randint(255) # currently random from 0-255, should be r value from camera
        g = random.randint(255) # g value from camera
        b = random.randint(255) # b value from camera
        array[x,y] = [r, g, b]

print(array[:width])
plt.imshow(array)
plt.show()