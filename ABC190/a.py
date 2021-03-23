A, B, C = map(int, input().split())
if C: # aoki
    while True:
        if not B:
            print('Takahashi')
            exit()
        B -= 1
        if not A:
            print('Aoki')
            exit()
        A -= 1
else:
    while True:
        if not A:
            print('Aoki')
            exit()
        A -= 1
        if not B:
            print('Takahashi')
            exit()
        B -= 1

