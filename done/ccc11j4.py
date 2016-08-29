visited = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5),
           (5, 5), (5, 4), (5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),
           (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7), (-1, 7), (-1, 6),
           (-1, 5)]

x = -1
y = 5

while True:
    d, n = input().split()
    n = int(n)
    danger = False
    if d == "q":
        break
    elif d == "d":
        for i in range(n):
            y += 1
            if (x, y) in visited:
                danger = True
            visited.append((x, y))
    elif d == "u":
        for i in range(n):
            y -= 1
            if (x, y) in visited:
                danger = True
            visited.append((x, y))
    elif d == "r":
        for i in range(n):
            x += 1
            if (x, y) in visited:
                danger = True
            visited.append((x, y))
    elif d == "l":
        for i in range(n):
            x -= 1
            if (x, y) in visited:
                danger = True
            visited.append((x, y))
    print("{} {} {}".format(x, -y, "DANGER" if danger else "safe"))
    if danger:
        break