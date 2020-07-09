n, k = map(int, input().split())
d = []
a = []
for _ in range(k):
    d.append(int(input()))
    a.append(list(map(int, input().split())))

sunuke = [0] * n

for candy in a:
    for i in candy:
        i -= 1
        sunuke[i] += 1

print(len([i for i in sunuke if i == 0]))
