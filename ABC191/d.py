import math

X, Y, R = map(float, input().split())

count = 0
pos_x = list(range(int(X-R), int(X+R+1)))
for x in pos_x:
    y_o = math.sqrt((R * R) - (x - X) * (x - X))
    y_p = int(y_o + Y)
    y_n = int(-y_o + Y)

    # pos_y = list(range(y_n, y_p+1))
    count += y_p+1 - y_n

print(count)
