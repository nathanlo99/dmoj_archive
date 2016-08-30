from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = set()
q = [1]
last = 1
while q:
    n = q[0]
    q = q[1:]
    for b in graph[n]:
        if b in v:
            continue
        v.add(b)
        last = b
        q.append(b)

q = [last]
d = {last: 0}
while q:
    n = q[0]
    q = q[1:]
    for b in graph[n]:
        if b in d:
            continue
        d[b] = d[n] + 1
        last = b
        q.append(b)
print(d[last])