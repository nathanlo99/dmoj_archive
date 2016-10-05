import bisect
import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())

p_sum = [0]
p_set = [[] for i in xrange(2001)]

for i, num in enumerate(map(int, input().split())):
    p_sum.append(p_sum[-1] + num)
    p_set[num + 1000].append(i)

def find_ge(a, x):
    i = bisect.bisect_left(a, x)
    if i == len(a):
        return 100000000
    return a[i]

for _ in xrange(q):
    a, b, x, y = map(int, input().split())
    if p_sum[y] - p_sum[x - 1] > k:
        pa = p_set[a + 1000]
        pb = p_set[b + 1000]
        if find_ge(pa, x - 1) <= y - 1 and find_ge(pb, x - 1) <= y - 1:
            print("Yes")
            continue
    print("No")