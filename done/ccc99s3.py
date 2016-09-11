def filled(x, y, i):
    size = 3 ** (i - 1)
    while size > 0:
        if x // size == 1 and y // size == 1:
            return False
        else:
            x, y, size = x % size, y % size, size // 3
    return True

for i in range(int(input())):
    d = int(input())
    b = int(input())
    t = int(input())
    l = int(input())
    r = int(input())
    for i in range(t - 1, b - 2, -1):
        line = ""
        for j in range(l - 1, r):
            if filled(i, j, d):
                line += "* "
            else:
                line += "  "
        print(line)
    print()