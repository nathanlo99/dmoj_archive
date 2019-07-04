farthest = (0, 0)
dist2 = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x * x + y * y > dist2:
        farthest = (x, y)
        dist2 = x * x + y * y
print(farthest[0], farthest[1])