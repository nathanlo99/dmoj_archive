from math import ceil
points = []
for i in range(int(input())): points.append(tuple(map(int, input().split())))
points.append(points[0])
a = sum(points[i][0] * points[i + 1][1] for i in range(len(points) - 1))
b = sum(points[i][1] * points[i + 1][0] for i in range(len(points) - 1))
a, b = max(a, b), min(a, b)
print(int(ceil(0.5 * (a - b))))
