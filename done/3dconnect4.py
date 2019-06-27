a = []
for i in range(6):
    r = []
    for j in range(6):
        r.append(input().strip())
    if i < 5:
        input()
    a.append(r)

ans = 0

d = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

for i in range(0, 6):
    for j in range(0, 6):
        for k in range(0, 6):
            if a[i][j][k] != "R":
                continue
            for dt in d:
                for t in range(0, 4):
                    nx, ny, nz = i + t * dt[0], j + t * dt[1], k + t * dt[2]
                    if 0 <= nx < 6 and 0 <= ny < 6 and 0 <= nz < 6:
                        if a[nx][ny][nz] != "R":
                            break
                    else:
                        break
                else:
                    ans += 1
                
print(ans if ans else "lost")