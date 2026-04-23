#Semantic-Segmentation-Loss-Functions
#binary_crossentropy
import numpy as np
predictions = np.array([[0.25,0.25,0.25,0.25],
                        [0.01,0.01,0.01,0.96]])
actual = np.array([[0,0,0,1],
                   [0,0,0,1]])
def binary_crossentropy(predictions, targets, epsilon=1e-10):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce_loss = -np.sum(np.sum(targets * np.log(predictions + 1e-5)))/N
    return ce_loss
binary_crossentropy_loss = binary_crossentropy(predictions, actual)
print ("Binary_Cross entropy loss is: " + str(binary_crossentropy_loss))