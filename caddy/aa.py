import math
N = int(input())
sqn = math.sqrt(N)

a = 1
hit = 0
hits = []
v = 0
while(True):
    b = 1
    a += 1
    if a > sqn:
        break
    while(True):
        b += 1
        v = a ** b 
        if v > N :
            break
        hit += 1
        hits.append(v)
print(N - len(set(hits)))