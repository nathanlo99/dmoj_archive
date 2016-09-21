import sys
input = sys.stdin.readline

num = sorted(int(input()) for i in xrange(int(input())))
ans = sum(num)
for i in xrange(len(num) - 3, -1, -3):
    ans -= num[i]
print(ans)