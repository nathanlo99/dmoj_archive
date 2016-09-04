import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    graph[a].append(b)

x, y = map(int, input().split())
q = [x]
visited = set()
while q:
    n = q[0]
    q = q[1:]
    if n not in graph:
        continue
    for a in graph[n]:
        if a in visited:
            continue
        visited.add(a)
        q.append(a)
    if y in visited:
        print("yes")
        sys.exit(0)

q = [y]
visited = set()
while q:
    n = q[0]
    q = q[1:]
    if n not in graph:
        continue
    for a in graph[n]:
        if a in visited:
            continue
        visited.add(a)
        q.append(a)
    if x in visited:
        break

if x in visited:
    print("no")
else:
    print("unknown")