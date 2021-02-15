x = int(input())

for i, n in enumerate(range(4, 19, 2)):
    r = 8 - i
    hi = n * 100 + 199
    low = n*100
    if low <= x <= hi:
        print(r)
        exit()

