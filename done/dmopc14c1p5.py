import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
sy, sx = map(int, input().split())
ty, tx = map(int, input().split())

grid = [list(input().strip()) for i in xrange(r)]

for _ in xrange(int(input())):
    x, y = map(int, input().split())
    grid[x][y] = "T"

q = deque([(sx, sy)])
d = {(sx, sy): 0}

min_tele = 100000000
if grid[sy][sx] == "T":
    min_tele = 0
    
while q:
    cx, cy = q.popleft()
    dd = d[(cx, cy)] + 1
    for x, y in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
        if x < 0 or x >= c or y < 0 or y >= r or grid[y][x] == "X" or (x, y) in d:
            continue
        d[(x, y)] = dd
        if grid[y][x] == "T":
            min_tele = min(min_tele, dd)
        q.append((x, y))

print(max(d[(tx, ty)] - min_tele, 0))