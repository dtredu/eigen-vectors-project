import numpy as np


def power_iteration(A, epsilon=1e-16, iter_limit=1e3):
    assert A.shape[0] == A.shape[1]
    n = A.shape[0]
    x = np.random.rand(n)
    c = 1e9
    last_c = -1e9
    i = 1
    while True:
        i += 1
        if np.abs(c - last_c) <= epsilon:
            return c, x
        if i > iter_limit:
            return None
        last_x = x
        last_c = c
        x = A @ last_x
        # c = x[0] / last_x[0]
        # c = x.T @ A @ x / (x.T @ x)
        c = np.dot(x, last_x) / np.dot(last_x, last_x)
        x /= np.linalg.norm(x)


def rotation_method(A, max_iter=1000, epsilon=1e-6):
    np.seterr(divide="ignore", invalid="ignore")
    n = A.shape[0]
    k = 0
    H_k = np.identity(n)
    A_k = np.copy(A)
    eigenvalues = []
    eigenvectors = []
    for _ in range(max_iter):
        max_element = 0
        max_i = 0
        max_j = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A_k[i][j]) > abs(max_element):
                    max_element = A_k[i][j]
                    max_i = i
                    max_j = j
        if abs(max_element) <= epsilon:
            break
        phi = 0.5 * np.arctan(2 * max_element / (A_k[max_i][max_i] - A_k[max_j][max_j]))
        H_k = np.identity(n)
        H_k[max_i][max_i] = np.cos(phi)
        H_k[max_i][max_j] = -np.sin(phi)
        H_k[max_j][max_i] = np.sin(phi)
        H_k[max_j][max_j] = np.cos(phi)
        A_k = np.dot(np.dot(np.transpose(H_k), A_k), H_k)
        k += 1
    for i in range(n):
        eigenvalues.append(A_k[i][i])
        eigenvectors.append(H_k[:, i])
    return eigenvalues, eigenvectors
