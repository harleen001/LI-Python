#Mean Absolute Error
import numpy as np
predictions = np.array([2.5, 0.0, 2, 8])
actual = np.array([3, -0.5, 2, 7])

print("p is: " + str(["%.8f" % elem for elem in predictions]))
print("a is: " + str(["%.8f" % elem for elem in actual]))

def mae(predictions, actual):
    difference = predictions - actual
    absolute_difference = np.absolute(difference)
    mean_absolute_difference = absolute_difference.mean()
    return mean_absolute_difference
mae_val = mae(predictions, actual)
print ("mae error is: " + str(mae_val))