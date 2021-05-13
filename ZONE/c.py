from itertools import combinations

N = int(input())
status = [tuple(map(int, input().split())) for _ in range(N)]

def calc(member):
    sta = []
    for i in range(5):
        sta.append(max(member[0][i], member[1][i], member[2][i]))
    return min(sta)

l = list(range(N))

ans = -100

for a, b, c in combinations(l, 3):
    ans = max(ans, calc([status[a], status[b], status[c]]))

print(ans)