import sys
input = sys.stdin.readline

import bisect
n = int(input())
d = sorted(map(int, input().split()))

def binary_search(a, x, lo, hi):
    pos = bisect.bisect_left(a, x, lo, hi)
    return pos != hi and a[pos] == x
ans = 0
for i in range(n):
    for j in range(i):
        a = d[j]
        b = d[i]
        if binary_search(d, 2 * b - a, i + 1, n):
            ans = 3 * b
print(ans)