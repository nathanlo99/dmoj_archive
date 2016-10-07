import sys
input = sys.stdin.readline

r, c = map(int, input().split())
l, w = map(int, input().split())
n = int(input())
vis = set()

for _ in range(n):
    x, y = map(int, input().split())
    vis.add((x, y))
    for yy, xx in vis:
        bad = False
        for dx in range(0, w):
            for dy in range(0, l):
                if (yy + dy, xx + dx) not in vis:
                    bad = True
                    break
            if bad:
                break
        else:
            print("Special store was found on:", _ + 1)
            sys.exit(0)
print("Special store was not located")