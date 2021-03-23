N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

sara = [0] * (N + 1)
sara[0] += 1

for k in range(2**(K-1)):
    

for c, d in CD:
    if sara[c] == 0:
        sara[c] += 1
    elif sara[d] == 0:
        sara[d] += 1

zeros = [i for i, x in enumerate(sara) if x == 0]

ok = [(a, b) for a, b in AB if a not in zeros and b not in zeros]
print(len(ok))
