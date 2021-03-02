import itertools

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

best_acc = 0

for cd in itertools.product(*CD):
    cd = set(cd)
    acc = sum([a in cd and b in cd for a, b in AB])
    if acc > best_acc:
        best_acc = acc

print(best_acc)
