n, k = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    if i + k >= n:
        exit()
    pre = A[i]
    aft = A[i+k]
    if pre >= aft:
        print('No')
    else:
        print('Yes')

