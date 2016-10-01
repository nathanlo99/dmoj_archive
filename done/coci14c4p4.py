import math
from collections import defaultdict
n = int(input())
pipes = defaultdict(list)

for i in range(n - 1):
    a, b, p, t = map(int, input().split())
    pipes[a - 1].append((b - 1, p, t))

r = list(map(int, input().split()))

def dfs(node):
    if r[node] != -1:
        return r[node]
    res = 0
    for child, percent, special in pipes[node]:
        needed = dfs(child)
        if special:
            ans = math.sqrt(needed) * (100. / percent)
        else:
            ans = needed * 100. / percent
        res = max(res, ans)
    return res

print("{:.3f}".format(dfs(0)))