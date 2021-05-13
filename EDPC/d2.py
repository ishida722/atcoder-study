N, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]

wv = sorted(wv, key=lambda x: x[1], reverse=True)

dp = []

for i in range(N):
    w = wv[i][0]
    v = wv[i][1]
    dp.append(max)