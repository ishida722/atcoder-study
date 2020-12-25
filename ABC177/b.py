s = input()
t = input()


def diff_count(a, b):
    c = 0
    for aa, bb in zip(a, b):
        if aa != bb:
            c += 1
    return c


min_d = len(t)

for i in range(len(s)-len(t)+1):
    ss = s[i:i + len(t)]
    d = diff_count(ss, t)
    if d < min_d:
        min_d = d

print(min_d)

