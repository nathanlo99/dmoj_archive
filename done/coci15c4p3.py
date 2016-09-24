n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
a = [0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if i > j:
            a[i] |= grid[i][j]
            a[j] |= grid[i][j]
print(" ".join(map(str, a)))