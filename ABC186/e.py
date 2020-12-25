T = int(input())
cases = [list(map(int, input().split())) for _ in range(T)]


def calc(n, s, k):
    amari = n & k
    nokori = n - s
    if amari == 0 and nokori & k != 0:
        print(-1)
        return
    print(1)


for c in cases:
    calc(*c)
