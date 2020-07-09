import sys

n = input()
a = list(map(int, input().split()))
sum_a = 1

if 0 in a:
    print(0)
    sys.exit()

for e in a:
    sum_a *= e
    if sum_a > 1e18:
        print(-1)
        sys.exit()

if sum_a > 1e18:
    sum_a = -1

print(sum_a)
