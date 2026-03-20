import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")
from skimage import io, feature
import matplotlib.pyplot as plt

# Load the image
image = io.imread('cat.webp', as_gray=True)

# Apply Local Binary Pattern (LBP)
lbp = feature.local_binary_pattern(image, P=8, R=1, method='uniform')

# Display the original image and the LBP result
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('LBP')
plt.imshow(lbp, cmap='gray')
plt.show()