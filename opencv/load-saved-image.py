import cv2
image_path = 'gfg-image.png'

img = cv2.imread(image_path)
filename = 'savedImage.jpg'

cv2.imwrite(filename, img)

img = cv2.imread(filename)
cv2.imshow("GeeksforGeeks", img)

cv2.waitKey(0)
cv2.destroyAllWindows()