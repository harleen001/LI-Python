#Mean Square Error
import numpy as np
predictied = np.array([2.5, 0.0, 2, 8])
actual = np.array([3, -0.5, 2, 7])
def rmse(predicted, actual):
    difference = predicted - actual
    difference_squared = difference ** 2
    mean_of_difference_squared = difference_squared.mean()
    rmse_val = np.sqrt(mean_of_difference_squared)
    return rmse_val
print("p is: " + str(["%.8f" % elem for elem in predictions]))
print("a is: " + str(["%.8f" % elem for elem in actual]))
rmse_val = rmse(predictions, actual)
print("rms error is: " + str(rmse_val))