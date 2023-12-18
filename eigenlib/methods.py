import numpy as np

def power_iteration(A,epsilon = 1e-6, iter_limit = 1e3):
  assert A.shape[0] == A.shape[1]
  n = A.shape[0]
  last_x = np.random.rand(n)
  x = A @ last_x
  c = x[0] / last_x[0]
  last_c = c + epsilon * 2
  i = 1
  while np.abs(c - last_c) > epsilon:
    i+=1
    if i >= iter_limit:
      return None
    last_x = x
    last_c = c
    x = A @ last_x
    c = x[0] / last_x[0]
    x /= np.linalg.norm(x)
    print(c,x)
  return c,x

