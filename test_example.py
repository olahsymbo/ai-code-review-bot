import numpy as np

def compute_cost(input_data, target, theta):
    target_size = len(target) 
    predictions = input_data.dot(theta)
    error = predictions - target
    cost = (1 / (2 * target_size)) * np.sum(error ** 2)
    return cost

def gradient_descent(input_data, target, theta, alpha, iterations):
    target_size = len(target)
    cost_history = []

    for _ in range(iterations):
        gradient = (1 / target_size) * input_data.T.dot(input_data.dot(theta) - target)
        theta -= alpha * gradient
        cost_history.append(compute_cost(input_data, target, theta))

    return theta, cost_history


if __name__ == "__main__":
  
  data = np.array([[1], [2], [3], [4], [5]]) 
  target = np.array([2, 4, 6, 8, 10]) 
  
  data_biased = np.c_[np.ones((len(data), 1)), data] 
  
  theta_init = np.random.randn(2, 1) 
  
  # Hyperparameters
  alpha = 0.01  
  iterations = 100
  
  theta_optimal, cost_history = gradient_descent(data_biased, target.reshape(-1, 1), theta_init, alpha, iterations)
  
  print("Optimized Theta (Weights):\n", theta_optimal)
