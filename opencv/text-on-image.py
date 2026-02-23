import cv2
image =cv2.imread('image.jpg')

output = image.copy()
text = cv2.putText(output, 'OpenCV Demo', (100, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

cv2.imshow("Rectangle",output)
cv2.waitKey(0)