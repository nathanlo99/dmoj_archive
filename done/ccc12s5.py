r, c = map(int, input().split())
cats = []
dp = [[0 for y in range(r + 1)] for x in range(c + 1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    cats.append((x, y))

for x in range(1, c + 1):
    for y in range(1, r + 1):
        if (x, y) == (1, 1):
            dp[x][y] = 1
        elif (y, x) in cats:
            dp[x][y] = 0
        else:
            dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
print(dp[c][r])