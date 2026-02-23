import cv2
image = cv2.imread('image.jpg')

roi = image[100 : 500, 200 : 700]
cv2.imshow("ROI", roi)
cv2.waitKey(0)