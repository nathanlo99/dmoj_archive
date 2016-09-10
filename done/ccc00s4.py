import sys
input = sys.stdin.readline

d = int(input())
clubs = [int(input()) for i in xrange(int(input()))]

dp = [100000 for i in xrange(d + 1)]
dp[0] = 0
for i in xrange(d + 1):
    if dp[i] != 100000:
        for club in clubs:
            if i + club <= d:
                dp[i + club] = min(dp[i + club], dp[i] + 1)
if dp[d] == 100000:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in {} strokes.".format(dp[d]))