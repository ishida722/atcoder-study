L = int(input())

L *= 10
ans = 0

for l in range(L):
    for w in range(L - l):
        h = L - l - w
        ans = max(ans, l / 10 * w / 10 * h / 10)

print(ans)
