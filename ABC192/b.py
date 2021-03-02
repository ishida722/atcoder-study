S = input()

for i, s in enumerate(S):
    i += 1
    if i % 2 == 1:
        if not s.islower():
            print('No')
            exit()
    else:
        if not s.isupper():
            print('No')
            exit()
print('Yes')