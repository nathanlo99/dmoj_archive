from collections import defaultdict
from bisect import bisect_left

px = defaultdict(list)
py = defaultdict(list)

for n in range(int(input())):
    x, y = map(int, input().split())
    px[x].append(y)
    py[y].append(x)

for v in px.values():
    v.sort()
for v in py.values():
    v.sort()

x_values = sorted(px.keys())
y_values = sorted(py.keys())

ans = 0
for xi, x in enumerate(x_values):
    if xi == 0 or xi == len(x_values) - 1:
        continue
    for yi, y in enumerate(px[x]):
        if yi == 0 or yi == len(px[x]) - 1:
            continue
        up = len(px[x]) - yi - 1
        down = yi
        left = bisect_left(py[y], x)
        right = len(py[y]) - left - 1
        ans += up * down * left * right

print(ans * 2)