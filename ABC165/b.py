x = int(input())
m = 100
n = 0

while True:
    n += 1
    m += int(m * 0.01)
    if m >= x:
        break

print(n)
