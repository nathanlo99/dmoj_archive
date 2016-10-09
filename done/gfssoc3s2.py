import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
px, py = -1, -1
bx, by = -1, -1
tx, ty = -1, -1

grid = []
for row in range(r):
    row_ = []
    for col, ch in enumerate(input().strip()):
        if ch == "P":
            px, py = col, row
        elif ch == "X":
            tx, ty = col, row
        elif ch == "B":
            bx, by = col, row
        row_.append("#" if ch == "#" else ".")
    grid.append(row_)

q = deque([(px, py, bx, by)])
dist = {(px, py, bx, by): 0}

while q:
    px, py, bx, by = q.popleft()
    d = dist[(px, py, bx, by)]
    if (bx, by) == (tx, ty):
        print(d)
        break

    neighbours = []
    if px >= 2 and (px - 1, py) == (bx, by):
        neighbours.append((px - 1, py, bx - 1, by))
    if px >= 1 and (px - 1, py) != (bx, by):
        neighbours.append((px - 1, py, bx, by))

    if px < c - 2 and (px + 1, py) == (bx, by):
        neighbours.append((px + 1, py, bx + 1, by))
    if px < c - 1 and (px + 1, py) != (bx, by):
        neighbours.append((px + 1, py, bx, by))

    if py >= 2 and (px, py - 1) == (bx, by):
        neighbours.append((px, py - 1, bx, by - 1))
    if py >= 1 and (px, py - 1) != (bx, by):
        neighbours.append((px, py - 1, bx, by))

    if py < r - 2 and (px, py + 1) == (bx, by):
        neighbours.append((px, py + 1, bx, by + 1))
    if py < r - 1 and (px, py + 1) != (bx, by):
        neighbours.append((px, py + 1, bx, by))

    for n in neighbours:
        if n in dist:
            continue
        nx, ny, nbx, nby = n
        if grid[ny][nx] == "#" or grid[nby][nbx] == "#":
            continue
        dist[n] = d + 1
        q.append(n)
else:
    print("-1")