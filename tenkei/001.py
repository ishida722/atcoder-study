import itertools

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

ans = -1

for kiri in itertools.permutations(A, K):
    kiri = sorted(kiri)
    ls = []
    pos = 0
    for k in kiri:
       ls.append(k-pos) 
       pos = k
    ls.append(L-pos) 
    ans = max(ans, min(ls))

print(ans)
