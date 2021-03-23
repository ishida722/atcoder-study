N, X = map(int, input().split())
VP = [tuple(map(int, input().split())) for _ in range(N)]

X = X * 100

alc = 0
n = 0

for v, p in VP:
    n += 1
    alc += v * p
    if alc > X:
        print(n)
        exit()
print(-1)