import math
x, y = 0.0, 0.0

for _ in range(int(input())):
    r, t = map(int, input().split())
    x += r * math.cos(math.radians(t))
    y += r * math.sin(math.radians(t))

r = round(math.hypot(x, y))
t = round(math.degrees(math.atan2(y, x))) % 360
print(r, t)