N = int(input())
ST = []
for _ in range(N):
    inputs = input().split()
    ST.append((inputs[0], int(inputs[1])))

print(sorted(ST, key=lambda x:x[1], reverse=True)[1][0])