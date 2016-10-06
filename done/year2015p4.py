va, vb, m = map(int, input().split())

q = [(0, 0)]
dist = {(0, 0): 0}
prev = {(0, 0): None}

while q:
    a, b = q[0]
    q = q[1:]
    d = dist[(a, b)]
    if a == m or b == m:
        instructions = []
        while (a, b) != (0, 0):
            step, (a, b) = prev[(a, b)]
            instructions.append(step)
        print("\n".join(instructions[::-1]))
        break
    if a != va and (va, b) not in dist:
        dist[(va, b)] = d + 1
        q.append((va, b))
        prev[(va, b)] = ("fill A", (a, b))
    if b != vb and (a, vb) not in dist:
        dist[(a, vb)] = d + 1
        q.append((a, vb))
        prev[(a, vb)] = ("fill B", (a, b))
    if a != 0 and (0, b) not in dist:
        dist[(0, b)] = d + 1
        q.append((0, b))
        prev[(0, b)] = ("chug A", (a, b))
    if b != 0 and (a, 0) not in dist:
        dist[(a, 0)] = d + 1
        q.append((a, 0))
        prev[(a, 0)] = ("chug B", (a, b))
    fillAB = min(a, vb - b)
    n = (a - fillAB, b + fillAB)
    if n not in dist:
        dist[n] = d + 1
        q.append(n)
        prev[n] = ("pour A B", (a, b))
    fillBA = min(b, va - a)
    n = (a + fillBA, b - fillBA)
    if n not in dist:
        dist[n] = d + 1
        q.append(n)
        prev[n] = ("pour B A", (a, b))
else:
    print("Not possible")