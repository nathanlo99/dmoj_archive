import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
graph = [-1 for i in range(m + 1)]
visited = set()
for i in range(n):
    a, b = map(int, input().split())
    if graph[b] == -1:
        graph[b] = a
while True:
    p = graph[p]
    if p in visited:
        print(-1)
        break
    visited.add(p)
    if p == -1:
        print(len(visited) - 1)
        break