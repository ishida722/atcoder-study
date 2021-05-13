N, D, H = map(int, input().split())
dh = [tuple(map(int, input().split())) for _ in range(N)]

a = float(H) / D

highest = 0
highest_h = -10000

for d, h in dh:
    hight = h - (a * d)
    if hight > highest_h:
        highest_h = hight
        highest = (d, h)

if highest_h <= 0:
    print(0)
    exit()

d, h = highest
a = float(h)/(D-d)
b = h - a * d

print(b)
