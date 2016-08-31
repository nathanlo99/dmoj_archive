n, m = map(int, input().split())

attacked = [[False for i in range(n)] for j in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(n):
        attacked[x][i] = True
        attacked[i][y] = True
    xx, yy = x, y
    while xx < n and yy < n:
        attacked[xx][yy] = True
        xx += 1
        yy += 1
    xx, yy = x, y
    while xx >= 0 and yy < n:
        attacked[xx][yy] = True
        xx -= 1
        yy += 1
    xx, yy = x, y
    while xx >= 0 and yy >= 0:
        attacked[xx][yy] = True
        xx -= 1
        yy -= 1
    xx, yy = x, y
    while xx < n and yy >= 0:
        attacked[xx][yy] = True
        xx += 1
        yy -= 1
#print("\n".join("".join(map(lambda x: "X" if x else " ", a)) for a in attacked))

c = 0
for i in range(n):
    for j in range(n):
        if not attacked[i][j]:
            c += 1
print(c)