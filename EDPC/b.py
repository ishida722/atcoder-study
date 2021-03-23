N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = []
current = 0

for i in range(N):
    if i == 0:
        dp.append(0)
    else:
        dp.append(min([dp[i-k] + abs(H[i-k]-H[i]) for k in range(1, min(K, i)+1)]))

print(dp[-1])