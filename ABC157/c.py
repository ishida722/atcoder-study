n, m = map(int, input().split())
SC = []
for _ in range(m):
    SC.append((map(int, input().split())))

ans = [-1] * n

for s, c in SC:
    s -= 1
    if ans[s] != -1:
        print(-1)
        exit()
    ans[s] = c

if ans[0] == 0:
    print(-1)
    exit()

aans = []
for a in ans:
    if a == -1:
        aans.append(0)
    else:
        aans.append(a)

print(aans)
