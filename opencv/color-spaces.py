import cv2
image = cv2.imread('parrot.webp')

image_rgb  = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv  = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_lab  = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow("Original BGR", image)
cv2.imshow("RGB Mode", image_rgb)
cv2.imshow("HSV Mode", image_hsv)
cv2.imshow("Grayscale", image_gray)
cv2.imshow("LAB Mode", image_lab)

cv2.waitKey(0)
cv2.destroyAllWindows()