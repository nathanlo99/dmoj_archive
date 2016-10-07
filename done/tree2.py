import sys
input = sys.stdin.readline

r, c = map(int, input().split())
trees = []
th = 0
x, y = -1, -1

grid = []
for row in range(r):
    tmp = []
    for col, j in enumerate(input().split()):
        if j == ".":
            tmp.append(0)
        elif j == "X":
            y, x = row, col
            tmp.append(0)
        else:
            if int(j) > th:
                th = int(j)
                trees = [(col, row)]
            elif int(j) == th:
                trees.append((col, row))
            tmp.append(int(j))
    grid.append(tmp)

tx, ty, min_dist = -1, -1, 1000000000
for treex, treey in trees:
    dist = (x - treex) ** 2 + (y - treey) ** 2
    if dist < min_dist:
        min_dist = dist
        tx, ty = treex, treey

q = []
dist = [[ 1000000 for i in range(r + 1) ] for j in range(c + 1) ]
dist[x][y] = 0
for row in range(r):
    for col in range(c):
        q.append((col, row))

while q:
    min_x, min_y, min_v = -1, -1, 100000000
    for x, y in q:
        if dist[x][y] < min_v:
            min_v = dist[x][y]
            min_x, min_y = x, y
    q.remove((min_x, min_y))
    d = dist[min_x][min_y]
    if (min_x, min_y) == (tx, ty):
        print(d % 10000 - 1)
        break
    for nx, ny in ((min_x - 1, min_y), (min_x + 1, min_y),
                   (min_x, min_y - 1), (min_x, min_y + 1)):
        if nx < 0 or nx >= c or ny < 0 or ny >= r:
            continue
        if dist[nx][ny] != 1000000:
            continue
        if grid[ny][nx] != 0:
            dist[nx][ny] = d + 1 + grid[ny][nx] * 10000
        else:
            dist[nx][ny] = d
        q.append((nx, ny))