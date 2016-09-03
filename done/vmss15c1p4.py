from collections import deque

t, n, m, g = map(int, input().split())

stores = []
roads = []

for i in range(n):
    roads.append({})

for _ in range(g):
    stores.append(int(input()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if c > t or a in roads and roads[a].get(b, -1) < c:
        continue
    roads[a][b] = c

distance = [None] * n
visited = [None] * n

q = []

distance[0] = 0
visited[0] = True
q.append(0)

while q:
    u = q[0]
    q = q[1:]
    for node in roads[u]:
        if node in q or visited[node]:
            continue
        if not distance[node] or distance[u] + roads[u][node] < distance[node]:
            distance[node] = distance[u] + roads[u][node]
        visited[node] = True
        q.append(node)

print(len([0 for x in range(n) if distance[x] != None and distance[x] <= t and x in stores]))