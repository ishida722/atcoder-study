H, W, X, Y = map(int, input().split())
S = [input().split() for _ in range(H)]

ans = 0
for i in range(W):
    w_count = 0
    
