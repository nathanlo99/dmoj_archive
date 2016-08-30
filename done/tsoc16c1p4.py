r, c = map(int, input().split())
g = [[] for i in range(r)]
for row in range(r):
    s = input()
    for col in s:
        g[row].append(col)

regions = []
rp = 0
def dfs(x, y, found):
    if g[y][x] == "#":
        return found
    if g[y][x] == "M":
        found = True
    g[y][x] = "#"
    if dfs(x - 1, y, found):
        found = True
    if dfs(x + 1, y, found):
        found = True
    if dfs(x, y - 1, found):
        found = True
    if dfs(x, y + 1, found):
        found = True
    return found

ans = 0
for i in range(1, r - 1):
    for j in range(1, c - 1):
        if dfs(j, i, False):
            ans += 1

print(ans)