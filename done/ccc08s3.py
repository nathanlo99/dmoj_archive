t = int(input())
for _ in range(t):
    r = int(input())
    c = int(input())
    grid = [[] for i in range(r)]
    for row in range(r):
        s = input().strip()
        for col in s:
            grid[row].append(col)
    # Moving from 0, 0 to r, c
    distance = {(0, 0) : 1}
    q = [(0, 0)]
    
    while q:
        x, y = q[0]
        q = q[1:]
        neighbours = []
        if grid[y][x] in "-+":
            neighbours.append((x - 1, y))
            neighbours.append((x + 1, y))
        if grid[y][x] in "|+":
            neighbours.append((x, y - 1))
            neighbours.append((x, y + 1))
        for xx, yy in neighbours:
            if (xx, yy) in distance:
                continue
            if xx < 0 or xx >= c or yy < 0 or yy >= r:
                continue
            if grid[yy][xx] == "*":
                continue
            distance[(xx, yy)] = distance[(x, y)] + 1
            q.append((xx, yy))
    print(distance.get((c - 1, r - 1), -1))