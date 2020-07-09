x, y = map(int, input().split())
a = int(- y / 2 + 2 * x)
b = int(y / 2 - x)

if a == 0 and b == 0:
    print('No')
elif a < 0 or b < 0:
    print('No')
elif a >= 0 and b >= 0:
    print('Yes')
else:
    print('No')
