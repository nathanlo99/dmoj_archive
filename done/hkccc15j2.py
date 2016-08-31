n = int(input())
points = []
min_max = 1000000
for i in range(n):
    x, y = map(int, input().split())
    for xx, yy in points:
        max_dist = max(abs(xx - x), abs(yy - y))
        if max_dist < min_max:
            min_max = max_dist
    points.append((x, y))
print(min_max * min_max)