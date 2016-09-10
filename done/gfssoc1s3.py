import sys
input = sys.stdin.readline
import itertools

n, m, t = map(int, input().split())
hiders = []
grid = []

for i in range(n):
    line = input()
    grid.append(line)
    for j, c in enumerate(line):
        if c == "H":
            hiders.append((j, i))
        if c == "G":
            start = (j, i)

ans = 1000000000000
for order in itertools.permutations(range(t)):
    x, y = start
    sub_ans = 0
    for hider in map(lambda x: hiders[x], order):
        q = [(x, y)]
        distance = {(x, y): 0}
        while q:
            cx, cy = q[0]
            q = q[1:]
            for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if (nx, ny) in distance:
                    continue
                if grid[ny][nx] == "X":
                    continue
                distance[(nx, ny)] = distance[(cx, cy)] + 1
                q.append((nx, ny))
            if hider in distance:
                sub_ans += distance[hider]
                break
        x, y = hider
    ans = min(ans, sub_ans)
print(ans)