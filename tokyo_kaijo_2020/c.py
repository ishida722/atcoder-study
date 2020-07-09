import numpy as np
from numba import njit


@njit
def get_a(n, a):
    b = np.zeros((n + 1), dtype=np.int64)
    for i in range(n):
        ai = a[i]
        l = max(0, i - ai)
        r = min(n, i + ai + 1)
        b[l] += 1
        b[r] -= 1
    return np.cumsum(b)[:n]


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = np.array(A, dtype=np.int64)
    for _ in range(K):
        A = get_a(N, A)
    print(*A)
