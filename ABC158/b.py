n, a, b = map(int, input().split())

total = 0
blue = 0

for i in range(int(10e100)):
    if i % 2 == 0:  # blue
        total += a
        blue += a
        if total >= n:
            mod = total - n
            print(blue - mod)
            break
    else:  # red
        total += b
        if total >= n:
            print(blue)
            break
