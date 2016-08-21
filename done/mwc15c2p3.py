input()
visited = set()
last = "O"
x, y = 0, 0
visited.add((x, y))
opposite = {"L": "R", "R": "L", "U": "D", "D": "U"}
for i, c in enumerate(input().split()):
    if c == "L":
        x -= 1
    elif c == "R":
        x += 1
    elif c == "U":
        y += 1
    elif c == "D":
        y -= 1
    if (x, y) in visited:
        print("Fell at {}".format(i + 1))
        break
    visited.add((x, y))
else:
    print("Safe!")
