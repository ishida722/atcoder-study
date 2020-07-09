def median(n, x):
    if n // 2 == 0:
        n_c = (n + 1) / 2
        return x[n_c]
    else:
        n_c_1 = n / 2
        n_c_2 = n / 2 + 1
        return (x[n_c_1] + x[n_c_2]) / 2


N = int(input())
ab = [list(map(int, input().split())) for i in range(N)]
