n = int(input())
for i in range(n):
    x, y, d = 0, 0, 0
    while True:
        op = int(input())
        if op == 0:
            break
        elif op == 1:
            dist = int(input())
            if d == 0:
                x += dist
            elif d == 1:
                y += dist
            elif d == 2:
                x -= dist
            elif d == 3:
                y -= dist
        elif op == 2:
            d = (d + 3) % 4
        elif op == 3:
            d = (d + 1) % 4
    print("Distance is {}".format(abs(x) + abs(y)))
    directions = []
    if x > 0:
        directions.append((2, x))
    elif x < 0:
        directions.append((0, -x))
    if y > 0:
        directions.append((3, y))
    elif y < 0:
        directions.append((1, -y))
    while directions:
        directions.sort(key=lambda x: min((x[0] - d + 4) % 4, (d - x[0] + 4) % 4), reverse=True)
        direction, amt = directions.pop()
        if (direction - d + 4) % 4 <= (d - direction + 4) % 4:
            while d != direction:
                d = (d + 1) % 4
                print(3)
        else:
            while direction != d:
                d = (d + 3) % 4
                print(2)
        print(1)
        print(amt)
    print()