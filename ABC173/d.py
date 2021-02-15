n = int(input())
A = list(map(int, input().split()))

circle = []
score = [0]
ans = 0


def check():
    global score
    score = []
    l = len(circle)
    if l == 0:
        score = [0]
        return
    for i in range(l):
        if i == l - 1:
            score.append(min(circle[i], circle[0]))
            continue
        score.append(min(circle[i], circle[i + 1]))


A.sort(reverse=True)

for a in A:
    max_score = max(score)
    circle.insert(score.index(max_score), a)
    ans += max_score
    check()

print(ans)
