n, a, b = map(int, input().split())

x, mod = divmod(n, a + b)

if x == 0:
    print(min(a, n))
else:
    print(a * x + min(mod, a))
