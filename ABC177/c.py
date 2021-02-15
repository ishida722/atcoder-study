import numpy as np

n = int(input())
A = list(map(int, input().split()))

ans = 0
mod = 1e9 + 7
A_cum = np.cumsum(A).tolist()
sum_ = sum(A)

for i in range(n-1):
    sum_ -= sum_ - A[i]
    ans += A[i] * sum_

print(int(ans % mod))
