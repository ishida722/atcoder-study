N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

XY = [i for i in XY if i[0] < S and i[1] > D]
if XY:
    print('Yes')
else:
    print('No')