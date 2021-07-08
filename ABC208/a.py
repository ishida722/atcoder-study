A, B = map(int, input().split())

maxx = 6 * A
minn = A

if A <= B <= maxx:
    print('Yes')
else:
    print('No')