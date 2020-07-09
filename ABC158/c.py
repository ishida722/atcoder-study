import math

a, b = map(int, input().split())

ax = math.floor(a/0.08)
bx = math.floor(b/0.1)

if ax == bx:
    print(ax)
    exit()

axs = [ax + i for i in range(13)]
bxs = [bx + i for i in range(10)]

xs = axs + bxs

l = [x for x in set(xs) if xs.count(x) > 1]

if len(l) == 0:
    print(-1)
else:
    print(min(l))
