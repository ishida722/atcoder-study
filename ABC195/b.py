A, B ,W = map(int, input().split())

m = 1e9
M = 0

for n in range(1, 1000001):
    if A*n<=1000*W and 1000*W<=B*n:
        m = min(m, n)
        M = max(M, n)

print('UNSATISFIABLE' if M==0 else f'{m} {M}')
