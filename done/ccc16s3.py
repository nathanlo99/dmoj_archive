import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [set() for i in range(n)]
deg = [0 for i in range(n)]

num_edges = n - 1
removed = set()

pho = [False for i in range(n)] # set(map(int, input().split()))
for i in map(int, input().split()):
    pho[i] = True

for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].add(b)
    adj[b].add(a)
    deg[a] += 1
    deg[b] += 1

# Make vertex-induced graph
q = deque([])
for i in xrange(n):
    if deg[i] == 1 and not pho[i]:
        q.append(i)

while q:
    v = q.popleft()
    if pho[v]:
        continue
    removed.add(v)
    deg[v] = 0
    for a in set(adj[v]):
        num_edges -= 1
        adj[a].remove(v)
        deg[a] -= 1
        if deg[a] == 1:
            q.append(a)

for i in xrange(n):
    if i not in removed:
        break

q = deque([i])
dist = {i: 0}
for i in removed:
    dist[i] = -1
    
while q:
    n = q.popleft()
    d = dist[n]
    for a in adj[n]:
        if a in dist:
            continue
        dist[a] = d + 1
        q.append(a)

q = deque([n])
dist = {n: 0}
for i in removed:
    dist[i] = -1
    
while q:
    n = q.popleft()
    d = dist[n]
    for a in adj[n]:
        if a in dist:
            continue
        dist[a] = d + 1
        q.append(a)

print(2 * num_edges - d)