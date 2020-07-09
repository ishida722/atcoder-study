N, A, B = map(int, input().split())
ans = 0

for n in range(N + 1):
    total_n = 0
    for i in str(n):
        total_n += int(i)
    if total_n < A:
        continue
    if total_n > B:
        continue
    ans += n

print(ans)
