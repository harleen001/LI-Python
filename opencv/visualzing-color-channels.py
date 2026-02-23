import cv2
import numpy as np

path = 'parrot.webp'
image = cv2.imread(path)

B, G, R = cv2.split(image)
cv2.imshow("Image",image)
cv2.imshow("Blue Image",B)
cv2.imshow("Green Image",G)
cv2.imshow("Red Image",R)
cv2.waitKey(0)

cv2.destroyAllWindows()