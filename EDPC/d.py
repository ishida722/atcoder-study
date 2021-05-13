N, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]

wv = sorted(wv, key=lambda x: x[1], reverse=True)

dp = []

for i in range(1, N+1):
    for j in range(W+1):
        w = wv[i][0]
        v = wv[i][1]
        if j - wv[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w+v])
        else:
            dp[i][j] = dp[i-1][j]

ans = dp[N][W]
