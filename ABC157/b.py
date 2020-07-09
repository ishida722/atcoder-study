import numpy as np

A = np.asarray([list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))])
n = int(input())
B = []
for _ in range(n):
    B.append(int(input()))

ans = np.zeros((3, 3))


def is_bingo(card) -> bool:
    if card[0, 0] == card[0, 1] == card[0, 2] == 1:
        return True
    if card[1, 0] == card[1, 1] == card[1, 2] == 1:
        return True
    if card[2, 0] == card[2, 1] == card[2, 2] == 1:
        return True
    if card[2, 0] == card[2, 1] == card[2, 2] == 1:
        return True
    if card[0, 0] == card[1, 0] == card[2, 0] == 1:
        return True
    if card[0, 1] == card[1, 1] == card[2, 1] == 1:
        return True
    if card[0, 2] == card[1, 2] == card[2, 2] == 1:
        return True
    if card[0, 0] == card[1, 1] == card[2, 2] == 1:
        return True
    if card[0, 2] == card[1, 1] == card[2, 0] == 1:
        return True
    return False


for b in B:
    if b in A:
        index = np.where(A == b)
        ans[index] = 1
    if is_bingo(ans):
        print('Yes')
        exit()
print('No')
