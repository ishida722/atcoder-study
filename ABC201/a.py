import itertools

A = list(map(int, input().split()))

for a1, a2, a3 in itertools.permutations(A, 3):
    if a3 - a2 == a2 - a1:
        print('Yes')
        exit()
print('No')