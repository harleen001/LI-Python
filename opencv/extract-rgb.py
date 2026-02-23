import cv2
image = cv2.imread('image.jpg')

h, w = image.shape[:2]

(B, G, R) = image[100, 100]  #moving 100 pixels from top and 100 pixels from right
print("R = {}, G = {}, B = {}".format(R, G, B))

B = image[100, 100, 0]
print("B = {}".format(B))