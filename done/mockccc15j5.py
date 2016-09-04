import sys
input = sys.stdin.readline

from bisect import bisect_right, bisect_left

n = int(input())
bx = {}
by = {}
for i in xrange(n):
    x, y = map(int, input().split())
    if x in bx:
        bx[x].append(y)
    else:
        bx[x] = [y]
    if y in by:
        by[y].append(x)
    else:
        by[y] = [x]
        
for v in bx.itervalues():
    v.sort()

for v in by.itervalues():
    v.sort()

m = int(input())
ans = 0
x, y = map(int, input().split())
for i in xrange(m - 1):
    nx, ny = map(int, input().split())
    if ny == y and y in by:
        a, b = min(nx, x), max(nx, x)
        ans += bisect_right(by[y], b) - bisect_left(by[y], a)
    elif nx == x and x in bx:
        a, b = min(ny, y), max(ny, y)
        ans += bisect_right(bx[x], b) - bisect_left(bx[x], a)
    x, y = nx, ny
print(ans)