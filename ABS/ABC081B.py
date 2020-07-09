n = int(input())
A = list(map(int, input().split()))


def all_even(lst):
    for a in lst:
        if a % 2 != 0:
            return False
    return True


ans = 0
while True:
    if not all_even(A):
        print(ans)
        break
    A = list(map(lambda a: a / 2, A))
    ans += 1

