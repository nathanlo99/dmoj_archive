import sys
input = sys.stdin.readline

word = input().strip()
n = len(word)

grid = [["." for i in range(4 * n + 1)] for j in range(5)]

moves = [(-2, 0), (-1, 1), (-1, -1), (0, -2), (0, 2), (1, 1), (1, -1), (2, 0)]
for i, v in enumerate(word):
    for dx, dy in moves:
        grid[2 + dy][4 * i + 2 + dx] = "#"
    grid[2][4 * i + 2] = v

for i, v in list(enumerate(word))[2::3]:
    for dx, dy in moves:
        grid[2 + dy][4 * i + 2 + dx] = "*"

for i in grid:
    print("".join(i))