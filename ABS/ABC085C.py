import sys

n, y = map(int, input().split())

for a in range(n+1):
    if a*10000 > y:
        continue
    for b in range(n-a+1):
        c = n - a - b
        if 10000 * a + 5000 * b + 1000 * c == y:
            print(a, b, c)
            sys.exit()

print(-1, -1, -1)
