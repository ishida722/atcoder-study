import itertools

S = input()

kouho = []

for i, s in enumerate(S):
    if s == 'x':
        continue
    kouho.append(i)

print(kouho)

print(len(set(itertools.permutations(kouho, 4))))
