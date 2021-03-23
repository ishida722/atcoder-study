N = int(input())
AT = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
X = list(map(int, input().split()))

def f(x, a, t):
    if t == 1:
        return x + a
    if t == 2:
        return max(x, a)
    return min(x, a)

for q in range(Q):
    ans = X[q]
    for n in range(N):
        ans = f(ans, *AT[n])
    print(ans)