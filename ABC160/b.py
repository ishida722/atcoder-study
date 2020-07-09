x = int(input())

c500, r500 = map(int, divmod(x, 500))
c5 = int(r500 / 5)

ans1 = c500 * 1000 + c5 * 5

print(ans1)
