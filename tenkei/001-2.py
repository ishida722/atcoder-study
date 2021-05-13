N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def solve(m):
    cnt = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= m and L - A[i] >= m:
            cnt += 1
            pre = A[i]
    if cnt >= K:
        return True
    return False

left = -1
right = L +1

while right - left > 1:
    mid = left + int((right - left)/2)
    if not solve(mid):
        right = mid
    else:
        left = mid

print(left)
