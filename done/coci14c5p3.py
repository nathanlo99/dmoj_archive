import sys
input = sys.stdin.readline

n, k = map(int, input().split())

x = [0 for i in range(100001)]
y = [0 for i in range(100001)]
a = [0 for i in range(200001)]
b = [0 for i in range(200001)]

max_t = 1
for i in range(n):
    xx, yy = map(int, input().split())
    x[xx] += 1
    y[yy] += 1
    a[xx + yy] += 1
    b[xx - yy + 100000] += 1
    max_t = max(max_t, x[xx], y[yy], a[xx + yy], b[xx - yy + 100000])
    if max_t == k:
        print(i + 1)
        break