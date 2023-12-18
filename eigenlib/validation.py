import numpy as np


def validate(A, eigenvalues, eigenvectors, epsilon=1e-6):
    n = len(eigenvalues)
    correct = [True] * n
    allcorrect = True
    for i in range(n):
        vec = (A @ eigenvectors[i]) / eigenvalues[i]
        diff = vec - eigenvectors[i]
        mx = np.max(np.abs(diff))
        if mx > epsilon:
            correct[i] = False
            allcorrect = False
    return allcorrect, correct
