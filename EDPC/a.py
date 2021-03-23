N = int(input())
H = list(map(int, input().split()))

dp = []

for i in range(N):
    if i >= 2:
        route_a = dp[i-1] + abs(H[i-1]-H[i])
        route_b = dp[i-2] + abs(H[i-2]-H[i])
        dp.append(min(route_a, route_b))
    elif i == 1:
        dp.append(abs(H[1]-H[0]))
    else:
        dp.append(0)
ans = dp[-1]
print(ans)

