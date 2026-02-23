import cv2
img = cv2.imread("gfg-image.png", cv2.IMREAD_COLOR)  #Only load color
cv2.imshow("GeeksforGeeks", img)
cv2.waitKey(0)   #window will close when user clicks

cv2.destroyAllWindows()   #destroy all other screens on closing