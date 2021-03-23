import numpy as np

N = int(input())
A = []
P = []
X = []
for _ in range(N):
    a, p, x = map(int, input().split())
    A.append(a)
    P.append(p)
    X.append(x)

A = np.array(A)
P = np.array(P)
X = np.array(X)

si = np.argsort(P)

for i in si:
    if A[i] >= X[i]:
        continue
    print(P[i])
    exit()
print(-1)


