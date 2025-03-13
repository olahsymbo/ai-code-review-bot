import numpy as np

def compute_cost(X, y, theta):
    m = len(y) 
    predictions = X.dot(theta)
    error = predictions - y
    cost = (1 / (2 * m)) * np.sum(error ** 2)
    return cost

def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    cost_history = []

    for _ in range(iterations):
        gradient = (1 / m) * X.T.dot(X.dot(theta) - y)
        theta -= alpha * gradient
        cost_history.append(compute_cost(X, y, theta))

    return theta, cost_history


if __name__ == "__main__":
  
  X = np.array([[1], [2], [3], [4], [5]]) 
  y = np.array([2, 4, 6, 8, 10]) 
  
  X_b = np.c_[np.ones((len(X), 1)), X] 
  
  theta_init = np.random.randn(2, 1) 
  
  # Hyperparameters
  alpha = 0.01  
  iterations = 100
  
  theta_optimal, cost_history = gradient_descent(X_b, y.reshape(-1, 1), theta_init, alpha, iterations)
  
  print("Optimized Theta (Weights):\n", theta_optimal)
