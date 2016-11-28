n = int(input())
d = [int(input()) for _ in range(n)]

dp = d[:]

for i in range(1, n):
    for j in range(0, i):
        if d[i] > d[j] and dp[i] < dp[j] + d[i]:
            dp[i] = dp[j] + d[i]

print(max(dp))