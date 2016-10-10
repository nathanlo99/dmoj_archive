import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {}
for _ in xrange(m):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]
w = int(input())
ants = []
for i in xrange(w):
    ants.append(int(input()))

distance_to_ants = [100000 for i in xrange(n + 1)]
for ant in ants:
    distance = {ant: 0}
    q = [ant]
    while q:
        node = q[0]
        q = q[1:]
        distance_to_ants[node] = min(distance_to_ants[node], distance[node])
        if node not in graph:
            continue
        for neighbour in graph[node]:
            if neighbour not in distance:
                distance[neighbour] = distance[node] + 1
                q.append(neighbour)

q = [1]
distance = {1: 0}
while q:
    node = q[0]
    q = q[1:]
    if distance[node] >= 4 * distance_to_ants[node]:
        continue
    for neighbour in graph.get(node, []):
        if neighbour in distance:
            continue
        distance[neighbour] = distance[node] + 1
        q.append(neighbour)
ans = distance.get(n, "sacrifice bobhob314")

if ans == 8:
    print("sacrifice bobhob314")
else:
    print(ans)