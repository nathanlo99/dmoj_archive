flooring = int(input())
R = int(input())
C = int(input())

floor = []
room_areas = []
vis = []

def fill(r, c):
    if r < 0 or r >= R or c < 0 or c >= C or floor[r][c] == "I" or vis[r][c]: return 0
    vis[r][c] = True
    return 1 + fill(r - 1, c) + fill(r + 1, c) + fill(r, c + 1) + fill(r, c - 1)

for _ in range(R):
    floor.append(input())
    vis.append([False] * C)

for row in range(R):
    for col in range(C):
        if not vis[row][col] and floor[row][col] == ".":
            room_areas.append(fill(row, col))

c = 0
for n in sorted(room_areas, reverse=True):
    if flooring < n: break
    flooring -= n
    c += 1

if c == 1: print(str(c) + " room, " + str(flooring) + " square metre(s) left over")
else: print(str(c) + " rooms, " + str(flooring) + " square metre(s) left over")
