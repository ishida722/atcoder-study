import collections

n = int(input())
votes = [input() for _ in range(n)]

v_coll = collections.Counter(votes).most_common()

most = v_coll[0][1]
mosts = []

for v, i in v_coll:
    if i == most:
        mosts.append(v)
    else:
        break

mosts.sort()

[print(m) for m in mosts]

