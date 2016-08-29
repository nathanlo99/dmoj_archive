graph = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]

a, b = map(int, input().split())
visited = [a]
q = [a]
while q:
    n = q[0]
    q = q[1:]
    for neighbour in graph.get(n, []):
        if neighbour in visited:
            continue
        visited.append(neighbour)
        q.append(neighbour)
if b not in visited:
    print("Not Tangled")
else:
    print("Tangled")