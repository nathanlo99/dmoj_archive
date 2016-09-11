import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
j = int(input())

p = [[0 for i in range(n + 1)] for i in xrange(3)]
for _ in range(j):
    xi, xf, i, t = map(int, input().split())
    p[t - 1][xi - 1] += i
    p[t - 1][xf] -= i
for t in range(3):
    x = 0
    ans = 0
    for n in p[t][:-1]:
        x += n
        if x < k:
            ans += 1
    print(ans)