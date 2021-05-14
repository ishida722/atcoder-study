from collections import deque

S = input()
T = deque()
rev = False

for s in S:
    if s == 'R':
        rev = not rev
    elif rev:
        if T and T[0] == s:
            T.popleft()
        else:
            T.appendleft(s)
    else:
        if T and T[-1] == s:
            T.pop()
        else:
            T.append(s)

if rev:
    T = reversed(T)

print("".join(T))