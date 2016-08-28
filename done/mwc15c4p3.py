import sys
input = sys.stdin.readline

n, q = map(int, input().split())
x = {}
y = {}
xy = set()

for i in range(n):
    xc, yc = map(int, input().split())
    x[xc] = x.get(xc, 0) + 1
    y[yc] = y.get(yc, 0) + 1
    xy.add((xc, yc))

for i in range(q):
    code, a, b = input().split()
    if code == "1":
        print("salty" if (int(a), int(b)) in xy else "bland")
    else:
        if a == "X":
            print(x.get(int(b), 0))
        else:
            print(y.get(int(b), 0))