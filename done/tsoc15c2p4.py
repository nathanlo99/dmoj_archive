n, m = map(int, input().split())
visited = [False for i in range(n)]
graph = [[] for i in range(n)]
dist = [9999999999 for i in range(n)]
count = [0 for i in range(n)]
in_deg = [0 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_deg[b] += 1

queue = []
for i, v in enumerate(in_deg):
    if v == 0:
        queue.append(i)
        dist[i] = 1
        count[i] = 1

paths = 0
ends = []

while queue:
    node = queue.pop()
    if visited[node]:
        continue
    visited[node] = True
    if len(graph[node]) == 0:
        paths = (paths + count[node]) % 1000000007
        ends.append((node, dist[node]))
    for neighbour in graph[node]:
        if dist[node] + 1 < dist[neighbour]:
            dist[neighbour] = dist[node] + 1
        in_deg[neighbour] -= 1
        if in_deg[neighbour] == 0:
            queue.append(neighbour)
        count[neighbour] += count[node]

print(paths)
print(" ".join(map(lambda x: str(x[1]), sorted(ends))))
