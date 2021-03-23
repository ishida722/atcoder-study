N, K = map(int, input().split())

def f(x):
    xs = map(int, str(x))
    g1 = sorted(xs, reverse=True)
    g2 = reversed(g1)

    g1 = int(''.join(map(str, g1)))
    g2 = int(''.join(map(str, g2)))
    # print(g1, g2)
    return g1 - g2

a = N

for k in range(K):
    a = f(a)

print(a)