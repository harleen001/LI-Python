import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

path1 = 'img/input1.jpg'
path2 = 'img/input2.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

added = cv2.add(img1, img2)
added_rgb = cv2.cvtColor(added, cv2.COLOR_BGR2RGB)

plt.imshow(added_rgb)
plt.title('Addition (cv2.add)')
plt.axis('off')
plt.show()