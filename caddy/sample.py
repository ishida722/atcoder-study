N, W = map(int, input().split())
VW = [tuple(map(int, input().split())) for _ in range(N)]

loop = 2 ** N
ans = 0
for i in range(loop):
    total_w = 0
    total_v = 0
    for j in range(N):
        if i >> j & 0x01 == 1:
            total_v += VW[j][0]
            total_w += VW[j][1]
            if total_w > W:
                total_v = 0
                break
    ans = max(ans, total_v)

print(ans)
