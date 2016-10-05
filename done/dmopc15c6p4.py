n, k = map(int, input().split())
edges = []
root = [i for i in range(k)]

def get_root(a):
    if root[a] != a:
        root[a] = get_root(root[a])
    return root[a]

def connect(a, b):
    ar = get_root(a)
    br = get_root(b)
    if ar != br:
        root[ar] = br

for i, v in enumerate(map(int, input().split())):
    edges.append((v, i, i + 1))
edges.sort()

i = 0
ans = 0
num_edges = 0
while i < len(edges) and num_edges < k - 1:
    v, a, b = edges[i]
    ar = get_root(a % k)
    br = get_root(b % k)
    if ar != br:
        root[ar] = br
        num_edges += 1
        ans += v
    i += 1

print(ans)