N = int(input())
A = list(map(int, input().split()))

ans = 0

for l in range(N):
    a = A[l]
    for r in range(l, N):
        a = min(a, A[r])
        mikan = a * (r-l+1)
        ans = max(ans, mikan)

print(ans)