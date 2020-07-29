n = int(input())
X = list(map(int, input().split()))
ans = 10000000000000000000000

for i in range(1, 101):
    cost = 0
    for x in X:
        cost += (i - x) ** 2
    if cost < ans:
        ans = cost

print(ans)
