N = int(input())

ans = 0

array = [int(str(i) + str(i)) for i in range(1, 1000000)]

for n in array:
    if n <= N:
        ans += 1
    else:
        print(ans)
        exit()