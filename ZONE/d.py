S = input()
T =''

for s in S:
    if s == 'R':
        T = T[::-1]
    else:
        T += s

def trim(T):
    ans = ''
    pre = ''
    flag = False
    for t in T:
        if pre == t:
            flag = True
            ans = ans[:-1]
            t = ''
        else:
            ans += t
        pre = t
    return ans, flag

while True:
    ans, flag = trim(T)
    T = ans
    if not flag:
        break

print(T)
