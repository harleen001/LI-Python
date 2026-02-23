import cv2

path = 'gfg-image.png'
src = cv2.imread(path)
window_name = 'GeeksforGeeks'

image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )

cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()