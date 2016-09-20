import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

n, c, k = map(int, input().split())
cherries = list(map(int, input().split()))
edges = {}
for i in xrange(n - 1):
    a, b, ki = map(int, input().split())
    a -= 1
    b -= 1
    if a in edges:
        edges[a].append((b, ki))
    else:
        edges[a] = [(b, ki)]
    if b in edges:
        edges[b].append((a, ki))
    else:
        edges[b] = [(a, ki)]

ans = 0
visited = set()
def solve(node):
    global visited, ans
    visited.add(node)
    node_cherries = cherries[node]
    node_weight = 0
    for neighbour, branch_weight in edges.get(node, []):
        if neighbour in visited:
            continue
        child_c, child_w = solve(neighbour)
        if child_c >= c and child_w + branch_weight <= k:
            ans += 1
        node_cherries += child_c
        node_weight += child_w + branch_weight
    return node_cherries, node_weight

solve(0)
print(ans)