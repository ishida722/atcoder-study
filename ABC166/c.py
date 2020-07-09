n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = []
for _ in range(m):
    ab.append(tuple(map(int, input().split())))

towers = [1] * n

for a, b in ab:
    a -= 1
    b -= 1
    a_hi = h[a]
    b_hi = h[b]
    if a_hi == b_hi:
        towers[a] = 0
        towers[b] = 0
    elif a_hi > b_hi:
        towers[b] = 0
    else:
        towers[a] = 0

print(len([i for i in towers if i == 1]))
