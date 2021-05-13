import numpy as np

H, W, A, B = map(int, input().split())

used = np.zeros((16, 16))

def dfs(i, j, a, b):
    if a < 0 or b < 0:
        return 0 # 敷き詰め失敗
    if j == W: # 行を変える
        j = 0
        i += 1
    if i == H:
        return 1 # 敷き詰め成功
    if used[i][j] == 1:
        return dfs(i, j+1, a, b) # すでに畳があったので次
    res = 0
    used[i][j] = 1
    res += dfs(i, j+1, a, b-1) # 半畳をつかう
    if j+1 < W and used[i][j+1] == 0: # 横に使う
        used[i][j+1] = 1
        res += dfs(i, j+1, a-1, b)
        used[i][j+1] = 0 # 探索が終わったら戻す
    if j+1 < H and used[i+1][j] == 0: # 縦に使う
        used[i+1][j] = 1
        res += dfs(i, j+1, a-1, b)
        used[i+1][j] = 0 # 探索が終わったら戻す
    used[i][j] = 0 # 探索が終わったら戻す
    return res

print(dfs(0, 0, A, B))