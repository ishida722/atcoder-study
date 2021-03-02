a, b, c = map(int, input().split())
k = int(input())


def ok(ax, bx, cx):
    if ax + bx + cx > k:
        return False
    aa = a
    bb = b
    cc = c
    for _ in range(ax):
        aa *= 2
    for _ in range(bx):
        bb *= 2
    for _ in range(cx):
        cc *= 2
    if aa < bb < cc:
        print('Yes')
        exit()
    else:
        return False


for x in range(8):
    ok(x, 0, 0)
    for y in range(8 - x):
        ok(x, y, 0)
        for z in range(8 - x - y):
            ok(x, y, z)
print('No')
