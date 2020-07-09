n = int(input())
A = list(map(int, input().split()))

alice = 0
bob = 0

A.sort(reverse=True)

for i in range(n):
    if i % 2 == 0:
        alice += A[i]
    else:
        bob += A[i]

print(alice-bob)

