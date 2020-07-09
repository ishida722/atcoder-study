import math

a, b = map(float, input().split())
a = int(a)
b = int(b * 100)
ab = (a * b) / 100.0
print(math.floor(ab))
