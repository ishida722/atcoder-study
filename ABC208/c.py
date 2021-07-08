N, K = map(int, input().split())
A = list(int, input().split())

A_sort = sorted(A)

normal, add = divmod(N, K)

border = A_sort[add-1]

for a in A:
    if a <= border:
        print(normal+1)
    else:
        print(normal)