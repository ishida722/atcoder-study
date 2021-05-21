S = input()
ans = 0
# 全ての数字を探索する
for i in range(10000):
    flag = [False]*10
    now = i
    # 対象の数値に含まれる数字にフラグを立てる。
    for _ in range(4):
        flag[now%10] = True
        now //= 10
    flag2 = True
    for j in range(10):
        # 使用されている数値の場合
        if S[j] == 'o' and not flag[j]:
            flag2 = False
        if S[j] == 'x' and flag[j]:
            flag2 = False
        if S[j] == '?' and flag[j]:
            flag2 = False
    ans += flag2
print(ans)
