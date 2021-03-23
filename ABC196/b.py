x = input()
if '.' not in x:
    print(x)
else:
    print(x[:x.find('.')])