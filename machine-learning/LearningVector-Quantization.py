import math

class LVQ:
    # Distance
    def winner(self, weights, sample):
        D0 = 0
        D1 = 0
        for i in range(len(sample)):
            D0 += (sample[i] - weights[0][i]) ** 2
            D1 += (sample[i] - weights[1][i]) ** 2
        return 0 if D0 > D1 else 1

    # Update
    def update(self, weights, sample, J, alpha, actual):
        if actual == J:
            for i in range(len(weights[0])):
                weights[J][i] += alpha * (sample[i] - weights[J][i])
        else:
            for i in range(len(weights[0])):
                weights[J][i] -= alpha * (sample[i] - weights[J][i])

# Main
def main():
    # Data
    X = [[0, 0, 1, 1], [1, 0, 0, 0],
         [0, 0, 0, 1], [0, 1, 1, 0],
         [1, 1, 0, 0], [1, 1, 1, 0]]
    Y = [0, 1, 0, 1, 1, 1]

    # Init
    weights = [X.pop(0), X.pop(0)]
    Y.pop(0)
    Y.pop(0)

    # Train
    lvq = LVQ()
    alpha = 0.1
    epochs = 3
    for _ in range(epochs):
        for i in range(len(X)):
            T = X[i]
            J = lvq.winner(weights, T)
            lvq.update(weights, T, J, alpha, Y[i])

    # Test
    T = [0, 0, 1, 0]
    J = lvq.winner(weights, T)
    print("Sample T belongs to class:", J)
    print("Trained weights:", weights)

if __name__ == "__main__":
    main()