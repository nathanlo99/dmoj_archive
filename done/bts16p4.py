import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
grid = []
for i in range(m):
    grid.append(list(input().strip()))
    if "O" in grid[-1]:
        x, y = grid[-1].index("O"), i

d = 0
for i in range(t):
    if d == 0:
        x += 1
    elif d == 1:
        y -= 1
    elif d == 2:
        x -= 1
    elif d == 3:
        y += 1
    if x < 0 or x >= n or y < 0 or y >= m:
        print("The observer leaves the grid after {} tick(s).".format(i + 1))
        break

    u = grid[y][x]
    if u == "/":
        d = [1, 0, 3, 2][d]
        grid[y][x] = "\\"
    elif u == "\\":
        d = [3, 2, 1, 0][d]
        grid[y][x] = "/"
    elif u == "-":
        d = [0, 3, 2, 1][d]
        if d in [1, 3]:
            grid[y][x] = "|"
    elif u == "|":
        d = [2, 1, 0, 3][d]
        if d in [0, 2]:
            grid[y][x] = "-"


else:
    print("The observer stays within the grid.")