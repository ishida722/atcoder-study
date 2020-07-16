import itertools

w, h, k = map(int, input().split())
C = [input() for _ in range(h)]

I = [f'i{i}' for i in range(h)]
J = [f'j{i}' for i in range(w)]

combi = []

for i in range(w+h):
    combi.extend(itertools.combinations(I + J, i))
