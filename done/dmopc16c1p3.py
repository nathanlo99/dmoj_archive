import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

memo = {}
input()
shoes = [int(x) for x in input().split()]

def solve(i):
    if i in memo:
        return memo[i]
    if i < 0:
        ans = 0
    elif i == 0:
        ans = shoes[0]
    elif i == 1:
        ans = shoes[0] + shoes[1] - min(shoes[0], shoes[1]) / 2
    else:
        ans = min(solve(i - 1) + shoes[i], \
                  solve(i - 2) + shoes[i] + shoes[i - 1] - min(shoes[i], shoes[i - 1]) / 2, \
                  solve(i - 3) + shoes[i] + shoes[i - 1] + shoes[i - 2] - min(shoes[i], shoes[i - 1], shoes[i - 2]))
    memo[i] = ans
    return ans

print("{:.1f}".format(solve(len(shoes) - 1)))