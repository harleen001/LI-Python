import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from itertools import cycle
from PIL import Image
#Segmentation of Color Image
# Replace 'sample.png' with the path to your image file
img = Image.open('Sample.jpg')
img = np.array(img)

#Need to convert image into feature array based
flatten_img=np.reshape(img, [-1, img.shape[-1]])
print(f"Shape of flattened image data: {flatten_img.shape}")

#bandwidth estimation
est_bandwidth = estimate_bandwidth(flatten_img,
quantile=.2, n_samples=500)
mean_shift = MeanShift(bandwidth=est_bandwidth, bin_seeding=True)
mean_shift.fit(flatten_img)
labels= mean_shift.labels_
print(f"Shape of labels array: {labels.shape}")



# Plot image vs segmented image
plt.figure(2)
plt.subplot(1, 2, 1) # Corrected subplot parameters for side-by-side display
plt.imshow(img)

plt.axis('off')
plt.subplot(1, 2, 2) # Corrected subplot parameters for side-by-side display

# Reshape labels to match image dimensions


plt.imshow(np.reshape(labels, [img.shape[0], img.shape[1]])) # Reshape labels to match image dimensions

plt.axis('off')
plt.show()