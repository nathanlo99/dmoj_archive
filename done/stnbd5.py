x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
k = float(input())
d = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
h = (k ** 2 - (0.5 * d) ** 2) ** 0.5

vx, vy = (y1 - y2) * h / d, (x2 - x1) * h / d
mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0

points = sorted([(mx + vx, my + vy), (mx - vx, my - vy)])

for x, y in points:
    print("{:.6f} {:.6f}".format(x, y))
    if h == 0:
        break