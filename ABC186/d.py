from numpy import cumsum

N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
A_cum = cumsum(A)

ans = 0

for n in range(1, N):
    ans += A[n] * n - A_cum[n - 1]

print(ans)
