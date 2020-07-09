n, k = map(int, input().split())

t = n % k
t2 = n - t

print(t) if t < t2 else print(t2)
