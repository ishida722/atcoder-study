import sys

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


c.sort(key=lambda e: e[0])

total = np.array([0] * (m + 1))

for book in c:
    total += book
    if ok(total[1:]):
        print(total[0])
        sys.exit()
print(-1)
