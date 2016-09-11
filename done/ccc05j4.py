w = int(input())
h = int(input())
cw = int(input())
ch = int(input())
steps = int(input())

grid = [[] for i in range(h + 2)]
for i in range(h + 2):
    for j in range(w + 2):
        if i == 0 or i == h + 1 or j == 0 or j == w + 1:
            grid[i].append("O")
        elif (i < ch + 1 or i > h - ch) and (j < cw + 1 or j > w - cw):
            grid[i].append("O")
        else:
            grid[i].append(".")
# print("\n".join("".join(x) for x in grid))

c = cw + 1
r = 1
d = 0

def move(r, c, d):
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    if grid[r + dy[d]][c + dx[d]] == ".":
        r += dy[d]
        c += dx[d]
        return r, c, d
    return -1, -1, -1

order = [[1, 0, 3, 2], [2, 1, 0, 3], [3, 2, 1, 0], [0, 3, 2, 1]]
for i in range(steps):
    grid[r][c] = "O"
    m = True
    for i in order[d]:
        rr, cc, dd = move(r, c, i)
        if dd != -1:
            d = dd
            r = rr
            c = cc
            break
    else:
        break

print(c)
print(r)