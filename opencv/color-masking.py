import cv2
import numpy as np

path = 'parrot.webp'
image = cv2.imread(path)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(image_hsv, lower_red1, upper_red1)

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(image_hsv, lower_red2, upper_red2)

full_mask = mask1 + mask2
result = cv2.bitwise_and(image, image, mask=full_mask)

print("--- ORIGINAL IMAGE ---")
cv2.imshow("Original",image)
    
print("\n--- THE MASK (Black = Ignored, White = Kept) ---")
cv2.imshow("Fullmask",full_mask)
    
print("\n--- FINAL RESULT (Red Extracted) ---")
cv2.imshow("Final",result)

cv2.waitKey(0)
cv2.destroyAllWindows()