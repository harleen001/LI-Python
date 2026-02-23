import cv2
image =cv2.imread('image.jpg')

output=image.copy()
rectangle=cv2.rectangle(output,(1500,900),(600,400),(255,0,0),2)

cv2.imshow("Rectangle",output)
cv2.waitKey(0)