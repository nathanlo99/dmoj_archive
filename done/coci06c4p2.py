a, b, c, d = map(int, input().split())
grid = []
for i in range(a):
    grid.append(input())

for i in range(a):
    for j in range(c):
        print("".join(d * ch for ch in grid[i]))