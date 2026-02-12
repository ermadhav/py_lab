import numpy as np


# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# AND gate training data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

y = np.array([[0], [0], [0], [1]])


# Initialize weights and bias
weights = np.random.rand(2, 1)
bias = np.random.rand(1)

learning_rate = 0.1


# Training the neural network
for epoch in range(10000):

    z = np.dot(X, weights) + bias
    y_pred = sigmoid(z)

    error = y - y_pred
    gradient = y_pred * (1 - y_pred)

    weights += learning_rate * np.dot(X.T, error * gradient)
    bias += learning_rate * np.sum(error * gradient)


# Testing
print("AND Gate Output:")

for i in X:
    output = sigmoid(np.dot(i, weights) + bias)
    print(i, "->", round(output[0]))