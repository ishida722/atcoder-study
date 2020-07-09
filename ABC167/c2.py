import numpy as np

n, m, x = map(int, input().split())
c = []
for _ in range(n):
    c.append(np.array(list(map(int, input().split()))))


def ok(lst):
    for tokuten in lst:
        if tokuten < x:
            return False
    return True


inf = 100000000000000000000
ans = inf

for s in range(n**2):
    cost = 0
    d = np.array([0] * m)
    for i in range(n):
        if s >> i & 1:
            cost += c[i][0]
            d += c[i][1:]
    if ok(d):
        ans = min(ans, cost)

if ans == inf:
    print(-1)
else:
    print(ans)
