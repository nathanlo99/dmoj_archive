n, h = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

q = [(0, 0)]
visited = set({(0, 0)})
while q:
    x, y = q[0]
    q = q[1:]
    z = grid[x][y]
    neighbours = []
    if x - 1 >= 0 and abs(grid[x - 1][y] - z) <= h:
        neighbours.append((x - 1, y))
    if x + 1 < n and abs(grid[x + 1][y] - z) <= h:
        neighbours.append((x + 1, y))
    if y - 1 >= 0 and abs(grid[x][y - 1] - z) <= h:
        neighbours.append((x, y - 1))
    if y + 1 < n and abs(grid[x][y + 1] - z) <= h:
        neighbours.append((x, y + 1))
    for ni in neighbours:
        if ni in visited:
            continue
        visited.add(ni)
        q.append(ni)
print("yes" if (n - 1, n - 1) in visited else "no")