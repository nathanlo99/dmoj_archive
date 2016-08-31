import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[-1 for i in xrange(m + 1)] for j in xrange(n + 1)]
for i in xrange(m + 1):
    dp[0][i] = 0
for i in xrange(n + 1):
    dp[i][0] = 0

for i in xrange(1, n + 1):
    for j in xrange(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])