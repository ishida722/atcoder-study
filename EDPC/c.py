N = int(input())
ABC = [tuple(map(int, input().split())) for _ in range(N)]
A = 0
B = 1
C = 2

dp = []
for i in range(N):
    if i > 0:
        scores = []
        # dp[i][j] : i日目に行動jをしてi日目までに得られる幸福度の和の最大値
        scores.append(max(dp[i-1][B], dp[i-1][C]) + ABC[i][A]) # i日目に A を選んだ B, C
        scores.append(max(dp[i-1][A], dp[i-1][C]) + ABC[i][B]) # B を選んだ A, C
        scores.append(max(dp[i-1][A], dp[i-1][B]) + ABC[i][C]) # C を選んだ A, B
        dp.append(scores)
    else:
        scores = []
        scores.append(ABC[i][A])
        scores.append(ABC[i][B])
        scores.append(ABC[i][C])
        dp.append(scores)


ans = max(dp[-1][A], dp[-1][B], dp[-1][C])
print(ans)