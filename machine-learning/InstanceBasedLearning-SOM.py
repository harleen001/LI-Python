import numpy as np
from minisom import MiniSom

# 1. Prepare your data
# Example: Generate some 2D data points for demonstration
data = np.random.rand(100, 2) * 10

# 2. Initialize the SOM
# x, y: dimensions of the SOM grid (e.g., 10x10 neurons)
# input_len: dimensionality of the input data (e.g., 2 for 2D data)
# sigma: neighborhood radius (controls how many neurons are updated around the BMU)
# learning_rate: initial learning rate for weight updates
som = MiniSom(x=10, y=10, input_len=2, sigma=1.0, learning_rate=0.5,
              neighborhood_function='gaussian', random_seed=0)

# 3. Initialize SOM weights (randomly or with PCA)
som.random_weights_init(data)
# or som.pca_weights_init(data) for PCA-based initialization

# 4. Train the SOM
# num_iteration: number of training iterations
som.train_random(data, num_iteration=100)

# 5. Use the trained SOM
# Get the Best Matching Unit (BMU) for a new data point
new_data_point = np.array([5.0, 5.0])
bmu = som.winner(new_data_point)
print(f"BMU for {new_data_point}: {bmu}")

# Get the weight vector of a specific neuron
neuron_weights = som.get_weights()[bmu[0], bmu[1]]
print(f"Weights of BMU: {neuron_weights}")