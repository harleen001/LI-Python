import cv2
image = cv2.imread('image.jpg')

resize = cv2.resize(image, (600, 600))
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)