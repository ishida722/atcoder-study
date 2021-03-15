N, M, Q = map(int, input().split())
WV = [tuple(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]

WV.sort(key=lambda x: x[1], reverse=True)
X


for l, r in queries:
    ans = 0
    l-=1
    r-=1
    boxes = X[:l] + X[r+1:]
    boxes.sort()
    for w, v in WV:
        for x in boxes:
            if x >= w:
                boxes.remove(x)
                ans += v
                break
    print(ans)
