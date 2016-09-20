n = int(input())
last = ""
ans = 0
dp = [0 for i in range(n)]
for i, name in enumerate(input().split()):
    if name[0] == last:
        ans += dp[i - 1] + 1
        dp[i] = dp[i - 1] + 1
    else:
        ans += 1
        dp[i] = 1
    last = name[0]
print(ans)