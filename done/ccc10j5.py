a, b = map(int, input().split())
c, d = map(int, input().split())

q = [(a, b)]
distance = {(a , b): 0}

while q:
    x, y = q[0]
    q = q[1:]
    neighbours = [ (x - 2, y - 1), (x - 2, y + 1),
                   (x - 1, y - 2), (x - 1, y + 2),
                   (x + 1, y - 2), (x + 1, y + 2),
                   (x + 2, y - 1), (x + 2, y + 1)]
    for nx, ny in neighbours:
        if (nx, ny) in distance:
            continue
        if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
            continue
        distance[(nx, ny)] = distance[(x, y)] + 1
        q.append((nx, ny))
print(distance[(c, d)])