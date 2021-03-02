n = int(input())
A = list(map(int, input().split()))

class Trade():
    def __init__(self):
        self.money = 1000
        self.option = 0

    def buy(self, price):
        if self.money == 0:
            return
        self.option = self.money // price
        self.money -= self.option * price

    def sell(self, price):
        if self.option == 0:
            return
        self.money += self.option * price
        self.option = 0


trade = Trade()

for i in range(n):
    if i == n-1:
        continue
    if A[i] < A[i+1]:
        trade.buy(A[i])
    else:
        trade.sell(A[i])

trade.sell(A[-1])

print(trade.money)
