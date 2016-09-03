import sys
input = sys.stdin.readline

m, n = map(int, input().split())
b = sorted((int(input()) for i in xrange(n)), reverse=True)

max_v = -10000000000
max_i = None
sum_ = sum(b) + m
num = n + 1
for i, v in enumerate(b):
    avg = sum_ / float(num)
    if m - avg > max_v:
        max_v = m - avg
        max_i = i
    sum_ -= v
    num -= 1
print(max_i)