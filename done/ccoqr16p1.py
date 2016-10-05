import sys
input = sys.stdin.readline

from collections import defaultdict
from bisect import bisect_left

px = defaultdict(list)
py = defaultdict(list)

for n in xrange(int(input())):
    x, y = map(int, input().split())
    px[x].append(y)
    py[y].append(x)

for v in px.values():
    v.sort()
for v in py.values():
    v.sort()

x_values = sorted(px.keys())

ans = 0
for xi, x in list(enumerate(x_values))[1:-1]:
    for yi, y in list(enumerate(px[x]))[1:-1]:
        up = len(px[x]) - yi - 1
        down = yi
        left = bisect_left(py[y], x)
        right = len(py[y]) - left - 1
        ans += up * down * left * right

print(ans * 2)