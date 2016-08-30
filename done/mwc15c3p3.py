n, q = map(int, input().split())
grid = [list(input().split()) for i in range(n)]


def find(grid, word, used, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if word == "":
        return True
    if grid[x][y] != word[0]:
        return False
    if (x, y) in used:
        return False
    used.append((x, y))
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if find(grid, word[1:], used, x + i, y + j):
                return True
    return False

def find_all(grid, word):
    for i in range(n):
        for j in range(n):
            if find(grid, word, [], i, j):
                return True
    return False


for _ in range(q):
    s = input()
    if len(s) > n * n:
        print("bad puzzle!")
        continue
    print("good puzzle!" if find_all(grid, s) else "bad puzzle!")