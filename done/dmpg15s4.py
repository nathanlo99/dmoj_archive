import sys
input = sys.stdin.readline

b, q = map(int, input().split())
graph = {}
beacons = []

for i in xrange(b):
    x, y, r = map(int, input().split())
    for j, (ax, ay, ar) in enumerate(beacons):
        dist_sqr = (ax - x) ** 2 + (ay - y) ** 2
        if dist_sqr <= ar ** 2:
            graph[j] = graph.get(j, []) + [i]
        if dist_sqr <= r ** 2:
            graph[i] = graph.get(i, []) + [j]
    beacons.append((x, y, r))

for _ in range(q):
    a, b = map(int, input().split())
    queue = [a - 1]
    visited = set()
    while queue:
        node = queue[0]
        queue = queue[1:]
        if node not in graph:
            continue
        for neighbour in graph[node]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            if neighbour == b - 1:
                break
            queue.append(neighbour)
        if b - 1 in visited:
            break
    print("YES" if b - 1 in visited else "NO")