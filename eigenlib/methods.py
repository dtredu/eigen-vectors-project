import numpy as np

def power_iteration(A,epsilon = 1e-16, iter_limit = 1e3):
  assert A.shape[0] == A.shape[1]
  n = A.shape[0]
  x = np.random.rand(n)
  c = 1e9
  last_c = -1e9
  i = 1
  while True:
    i+=1
    if np.abs(c - last_c) <= epsilon:
      return c,x
    if i > iter_limit:
      return None
    last_x = x
    last_c = c
    x = A @ last_x
    #c = x[0] / last_x[0]
    #c = x.T @ A @ x / (x.T @ x)
    c = np.dot(x,last_x) / np.dot(last_x,last_x)
    x /= np.linalg.norm(x)
