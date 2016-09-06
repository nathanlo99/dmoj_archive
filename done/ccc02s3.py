r = int(input())
c = int(input())
grid = [[] for i in range(r)]
for row in range(r):
    for col in input().strip():
        grid[row].append(col)

directions = ""
n = int(input())
for i in range(n):
    directions += input()[0]

for row in range(r):
    for col in range(c):
        if grid[row][col] != "X":
            for d in range(4):
                x, y = col, row
                for m in directions:
                    if m == "R":
                        d = (d + 3) % 4
                    elif m == "L":
                        d = (d + 1) % 4
                    elif m == "F":
                        if d == 0:
                            y += 1
                        elif d == 1:
                            x += 1
                        elif d == 2:
                            y -= 1
                        else:
                            x -= 1
                    if x < 0 or x >= c or y < 0 or y >= r or grid[y][x] == "X":
                        flag = False
                        break
                else:
                    grid[y][x] = "*"
print("\n".join("".join(x) for x in grid))