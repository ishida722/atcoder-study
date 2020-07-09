n, m = map(int, input().split())
A = list(map(int, input().split()))

line = sum(A)/(4 * m)

A = [a for a in A if a >= line]

print('Yes') if len(A) >= m else print('No')
