import sys
input = sys.stdin.readline

graph = {}
edges = []
s = input().strip()
while s != "**":
    edges.append(s)
    a, b = s
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]
    s = input().strip()

ans = 0
for a, b in edges:
    q = ["A"]
    visited = set("A")
    while q:
        n = q[0]
        q = q[1:]
        for c in graph.get(n, []):
            if c in visited:
                continue
            if n == a and c == b:
                continue
            if c == a and n == b:
                continue
            visited.add(c)
            q.append(c)
        if "B" in visited:
            break
    if "B" not in visited:
        print(a + b)
        ans += 1
print("There are {} disconnecting roads.".format(ans))