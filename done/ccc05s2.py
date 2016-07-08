c, r = map(int, input().split())
x, y = map(int, input().split())
mx, my = 0, 0
while x is not 0 or y is not 0:
    mx = max(0, min(mx + x, c))
    my = max(0, min(my + y, r))
    print(mx, my)
    x, y = map(int, input().split())
