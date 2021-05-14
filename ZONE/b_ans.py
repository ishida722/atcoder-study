N, D, H = map(int, input().split())
dh = [tuple(map(int, input().split())) for _ in range(N)]

def bill_pos(d, h):
    return h - d * (H-h) / (D-d)

print(max(0, *[bill_pos(d, h) for d, h in dh]))