import math

P = int(input())

coins = [math.factorial(i) for i in range(1, 11)]
coins.reverse()

count = 0
for c in coins:
    use, amari = divmod(P, c) 
    count += use
    P = amari

print(count)