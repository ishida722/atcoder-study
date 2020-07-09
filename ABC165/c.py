from collections import deque

n, m, q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(q)]


def calc(x):
    ans = 0
    for a, b, c, d in A:
        if int(x[b - 1]) - int(x[a - 1]) == c:
            ans += d
    return ans


q = deque([[1]])
ans = 0
while q:
    tmp = q.popleft()
    if len(tmp) == n:
        ans = max(ans, calc(tmp))
    else:
        for i in range(tmp[-1], m+1):
            q.append(tmp+[i])

print(ans)
