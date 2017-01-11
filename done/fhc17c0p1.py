import math
t = int(input())
for n in range(1, t + 1):
    print("Case #{}: ".format(n), end="")
    p, y, x = map(int, input().split())
    if p == 0 or (x - 50) ** 2 + (y - 50) ** 2 > 2500:
        print("white")
        continue
    if (x, y) == (50, 50):
        print("white" if p == 0 else "black")
    angle = math.degrees(math.atan2(y - 50, x - 50))
    if angle < 0:
        angle += 360
    if angle <= p * 3.6:
        print("black")
    else:
        print("white")