import sys
input = sys.stdin.readline

n = int(input())
x, y, z = sorted(map(int, input().split()))

t = [0] + [-999999 for i in xrange(n)]
for i in range(n + 1):
    m = t[i]
    if i >= x:
        m = max(m, t[i - x] + 1)
    if i >= y:
        m = max(m, t[i - y] + 1)
    if i >= z:
        m = max(m, t[i - z] + 1)
    t[i] = m

print(t[n])