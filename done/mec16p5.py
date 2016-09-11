import sys
input = sys.stdin.readline

def cross(a, b, p):
    return (a[0] - p[0]) * (b[1] - p[1]) - (a[1] - p[1]) * (b[0] - p[0])

hull = []
n = int(input())
for x in xrange(1, n + 1):
    y = int(input())
    while len(hull) >= 2 and cross(hull[-2], hull[-1], (x, y)) > 0:
        hull.pop()
    hull.append((x, y))

ans = 0.0
for i in xrange(0, len(hull) - 1):
    ans += ((hull[i][0] - hull[i + 1][0]) ** 2 + (hull[i][1] - hull[i + 1][1]) ** 2) ** 0.5

print("{:.1f}".format(ans))