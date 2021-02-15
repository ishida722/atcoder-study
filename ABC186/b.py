import numpy as np

h, w = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(h)])

A_diff = np.subtract(A, A.min())
print(A_diff.sum())
