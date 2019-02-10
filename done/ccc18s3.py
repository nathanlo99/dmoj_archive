from collections import deque
from pprint import pprint
import sys

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
num_dot = 0
start = None
bad = False

for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char == 'S':
            start = (col, row)
        elif char == 'C':
            new_row = row + 1
            while grid[new_row][col] != 'W':
                if grid[new_row][col] == '.':
                    grid[new_row][col] = 'X'
                if start == (col, new_row):
                    bad = True
                new_row += 1
            new_row = row - 1
            while grid[new_row][col] != 'W':
                if grid[new_row][col] == '.':
                    grid[new_row][col] = 'X'
                if start == (col, new_row):
                    bad = True
                new_row -= 1
            new_col = col + 1
            while grid[row][new_col] != 'W':
                if grid[row][new_col] == '.':
                    grid[row][new_col] = 'X'
                if start == (new_col, row):
                    bad = True
                new_col += 1
            new_col = col - 1
            while grid[row][new_col] != 'W':
                if grid[row][new_col] == '.':
                    grid[row][new_col] = 'X'
                if start == (new_col, row):
                    bad = True
                new_col -= 1

def follow_conveyors(x, y, seen=set()):
    if (x, y) in seen:
        return None
    dir = grid[y][x]
    seen.add((x, y))
    if dir == 'U':
        return follow_conveyors(x, y - 1, seen)
    elif dir == 'D':
        return follow_conveyors(x, y + 1, seen)
    elif dir == 'L':
        return follow_conveyors(x - 1, y, seen)
    elif dir == 'R':
        return follow_conveyors(x + 1, y, seen)
    elif dir in '.S':
        return (x, y)
    else:
        return None

dist = {start: 0}
q = deque()
q.append(start)

while q:
    x, y = q.popleft()
    neighbours = (follow_conveyors(x + dx, y + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)))
    for neighbour in neighbours:
        if neighbour is not None and neighbour not in dist:
            dist[neighbour] = dist[(x, y)] + 1
            q.append(neighbour)

for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char in ".X":
            print(dist.get((col, row), -1) if not bad else -1)