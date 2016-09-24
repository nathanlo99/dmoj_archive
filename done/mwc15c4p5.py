import bisect
import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())

v = set({0, x})
h = {}
for i in xrange(n):
    s = input()
    if s[0] == "h":
        y, x = map(int, s[1:].split())
        if (y in h and x > h[y]) or y not in h:
            h[y] = x
    else:
        x = int(s[1:])
        v.add(x)
        
v = sorted(list(v))
ans = len(v) - 1
for y in sorted(h.keys()):
    ans += bisect.bisect_right(v, h[y]) - 1
print(ans)