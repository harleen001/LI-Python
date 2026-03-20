import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('cat.webp') # Use an image with distinct features (e.g., a building or a car)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect SIFT keypoints
sift = cv2.SIFT_create()
keypoints = sift.detect(gray, None)

# Draw keypoints on the image
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the image with keypoints
plt.figure(figsize=(10, 5))
plt.title('SIFT Keypoints')
plt.imshow(cv2.cvtColor(image_with_keypoints, cv2.COLOR_BGR2RGB))
plt.show()