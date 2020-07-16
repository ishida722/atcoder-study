n = int(input())
S = [input() for _ in range(n)]

num_ac, num_wa, num_tle, num_re = 0, 0, 0, 0

for s in S:
    if s == 'AC':
        num_ac += 1
    elif s == 'WA':
        num_wa += 1
    elif s == 'TLE':
        num_tle += 1
    else:
        num_re += 1

print(f'AC x {num_ac}')
print(f'WA x {num_wa}')
print(f'TLE x {num_tle}')
print(f'RE x {num_re}')
