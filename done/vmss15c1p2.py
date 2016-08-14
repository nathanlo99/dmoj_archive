def dfs(node, graph):
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited[neighbour] = True
            dfs(neighbour, graph)

r, c = map(int, input().split(' '))

visited = {}
graph = {}
last = None

for i in range(r):
    row = input()
    n = [i * c + x for x in range(c) if row[x] == '.']
    for node in n:
        graph[node] = []
        if node != 0 and node - 1 in n:
            graph[node] += [node - 1]
            graph[node - 1] += [node]
        if last and last[node % c] == '.':
            graph[node] += [node - c]
            graph[node - c] += [node]
    last = row

treasures = 0

for node in graph:
    if node not in visited:
        visited[node] = True
        treasures += 1
        dfs(node, graph)

print(treasures)
