n, k = map(int, input().split())

while True:
    a = n
    n = abs(n-k)
    if n >= a:
        print(a)
        break
