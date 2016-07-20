n = int(input())
minx, miny = map(int, input().split())
maxx, maxy = (minx, miny)
for i in range(n - 1):
    x, y = map(int, input().split())
    if x < minx: minx = x
    if x > maxx: maxx = x
    if y < miny: miny = y
    if y > maxy: maxy = y
print(max(maxy - miny, maxx - minx) ** 2)
