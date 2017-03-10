x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = {}
y = {}

x[x1] = x.get(x1, 0) + 1
x[x2] = x.get(x2, 0) + 1
x[x3] = x.get(x3, 0) + 1

y[y1] = y.get(y1, 0) + 1
y[y2] = y.get(y2, 0) + 1
y[y3] = y.get(y3, 0) + 1

for xx in x.keys():
    if x[xx] == 1:
        print(xx, end=" ")

for yy in y.keys():
    if y[yy] == 1:
        print(yy)