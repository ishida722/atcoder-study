A, B, W = map(int, input().split())

W = W * 1000

n = 0

def search_min():
    for a in range(A, B+1):
        current_W = W
        n, current_W = divmod(current_W, a)
        for b in range(a+1, B+1):
            if current_W < b:
                break
            nn, current_W = divmod(current_W, b)
            n += nn
            if current_W == 0:
                return n
    return -1

def search_max():
    for a in range(B, A, -1):
        current_W = W
        n, current_W = divmod(current_W, a)
        for b in range(a, A, -1):
            if current_W < b:
                break
            nn, current_W = divmod(current_W, b)
            n += nn
            if current_W == 0:
                return n
    return -1
    
min_n = search_min()
max_n = search_max()

print(min_n, max_n)