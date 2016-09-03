n = int(input())
dp = [1 for i in range(7)]
for i in range(1, n):
    dp[int(input())] *= 1 + dp[i]
print(dp[n])