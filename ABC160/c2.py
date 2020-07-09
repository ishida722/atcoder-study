k, n = map(int, input().split())
A = list(map(int, input().split()))

A_dis = [a - A[i-1] if i > 0 else 0 for i, a in enumerate(A)]

A_dis.append(k - A[-1] + A[0])

A_dis.remove(max(A_dis))

print(sum(A_dis))
