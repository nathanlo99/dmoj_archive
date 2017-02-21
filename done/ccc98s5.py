t = int(input())
for _ in range(t):
    n = int(input())
    grid = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i].append(int(input()))
    oxygen = grid[0][0]
    distance = {(0, 0): 0}
    q = [(0, 0)]
    while q:
        x, y = q[0]
        q = q[1:]
        h = grid[x][y]
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (nx, ny) in distance:
                continue
            if abs(grid[nx][ny] - h) > 2:
                continue
            if grid[nx][ny] > oxygen or h > oxygen:
                distance[(nx, ny)] = distance[(x, y)] + 1
            else:
                distance[(nx, ny)] = distance[(x, y)]
            q.append((nx, ny))
    print(distance.get((n - 1, n - 1), "CANNOT MAKE THE TRIP"))
    print()