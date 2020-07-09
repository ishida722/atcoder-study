import itertools
import sys

s = input()
L = ['dreamer', 'dream', 'eraser', 'erase']

for l in itertools.permutations(L):
    ss = s
    for w in l:
        ss = ss.replace(w, '')
    if len(ss) == 0:
        print('YES')
        sys.exit()

print('NO')

