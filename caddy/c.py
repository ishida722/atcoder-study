K = int(input())
S = [int(i) for i in input() if i != '#']
T = [int(i) for i in input() if i != '#']

def calc(c):
    point = 0
    for i in range(1, 10):
        point += i * 10 ** c.count(i)
    return point

deck = [0]

for i in range(1, 10):
    deck.append(k - (S.count(i) + T.count(i)))



