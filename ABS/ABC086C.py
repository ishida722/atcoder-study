n = int(input())
T = []
for _ in range(n):
    T.append(list(map(int, input().split())))


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


pos = (0, 0)
for t, x, y in T:
    d = distance(pos, (x, y))
    if d > t or not (d + t) % 2 == 1:
        print('No')
        exit()
    pos = (x, y)

print('Yes')
