import sys
input = sys.stdin.readline

for _ in xrange(10):
    n, l = map(int, input().split())
    grid = [[] for i in xrange(n)]
    for i in range(n):
        for j in input().strip():
            grid[i].append(j)
    
    ans = 0
    for y in xrange(n - l + 1):  # Vertical boats
        for x in xrange(n):
            close = False
            for h in range(l):
                if grid[y + h][x] == "m":
                    close = True
                    break
            if close:
                continue
            if y - 1 >= 0 and grid[y - 1][x] == "h":
                continue
            if y + l < n and grid[y + l][x] == "h":
                continue
            if x - 1 >= 0:
                for h in xrange(-1, l + 1):
                    if 0 <= y + h < n and grid[y + h][x - 1] == "h":
                        close = True
                        break
            if x + 1 < n:
                for h in xrange(-1, l + 1):
                    if 0 <= y + h < n and grid[y + h][x + 1] == "h":
                        close = True
                        break
            if not close:
                # print("Vertical {}, {}".format(x, y))
                ans += 1
    
    for x in xrange(n - l + 1): # Horizontal
        for y in xrange(n):
            close = False
            for h in xrange(l):
                if grid[y][x + h] == "m":
                    close = True
                    break
            if close:
                continue
            if x - 1 >= 0 and grid[y][x - 1] == "h":
                continue
            if x + l < n and grid[y][x + l] == "h":
                continue
            if y - 1 >= 0:
                for h in xrange(-1, l + 1):
                    if 0 <= x + h < n and grid[y - 1][x + h] == "h":
                        close = True
                        break
            if y + 1 < n:
                for h in xrange(-1, l + 1):
                    if 0 <= x + h < n and grid[y + 1][x + h] == "h":
                        close = True
                        break
            if not close:
                # print("Horizontal {}, {}".format(x, y))
                ans += 1
    if l == 1:
        ans //= 2
    print(ans)