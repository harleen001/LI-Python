import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

path1 = 'img\input1.jpg'
path2 = 'img\input2.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
4
if img1 is None or img2 is None:
    print(f"ERROR: Could not find images!")
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"Looking for: {path1} and {path2}")
    exit()

if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

line_thickness = 5
height = img1.shape[0]
line = np.full((height, line_thickness, 3), (0, 0, 255), dtype=np.uint8)

side_by_side = np.hstack((img1, line, img2))
side_by_side_rgb = cv2.cvtColor(side_by_side, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))
plt.imshow(side_by_side_rgb)
plt.title('Comparison: Input 1 vs Input 2')
plt.axis('off')
plt.show()