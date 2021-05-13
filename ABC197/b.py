import numpy as np
H, W, X, Y = map(int, input().split())
S = [[0 if s=='.' else 1 for s in input()] for _ in range(H)]

ans = 0

for x in range(X, 0, -1):
    if S[x-1][Y-1] == 0:
        ans += 1
    else:
        break
for x in range(X, H):
    if S[x-1][Y-1] == 0:
        ans += 1
    else:
        break
for y in range(Y, 0, -1):
    if S[X-1][y-1] == 0:
        ans += 1
    else:
        break
for y in range(Y, W):
    if S[X-1][y-1] == 0:
        ans += 1
    else:
        break

print(ans-3)