n, m = map(int, input().split())
SC = []
for _ in range(m):
    SC.append(list(map(int, input().split())))

if n == 1:
    r = range(10)
if n == 2:
    r = range(10, 100)
else:
    r = range(100, 1000)


def is_ok(num_str):
    for s, c in SC:
        s -= 1
        if num_str[s] != str(c):
            return False
    return True


for num in r:
    num = str(num)
    if is_ok(num):
        print(num)
        exit()
print(-1)
