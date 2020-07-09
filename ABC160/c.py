k, n = map(int, input().split())
A = list(map(int, input().split()))

k_h = k / 2
pos = 0
ans = 0
for i in range(n):
    r = A[i] - pos
    l = k - r
    ans += min(r, l)
    pos += r

print(ans)
