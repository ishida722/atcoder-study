N = int(input())


def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


ans = 0

for n in range(1, N+1):
    if '7' in str(n):
        continue
    if '7' in Base_10_to_n(n, 8):
        continue
    ans += 1

print(ans)
