import sys

a, b, c, k = map(int, input().split())

nokori = k - a

if nokori <= 0:
    print(k)
    sys.exit()

nokori = nokori - b

if nokori <= 0:
    print(a)
    sys.exit()

print(a - nokori)

