import sys
input = sys.stdin.readline
n, t = map(int, input().split())
c = 0
for _ in xrange(n):
    a, b = map(int, input().split())
    if a * (100 - b) <= t * 100:
        c += 1
print(c)