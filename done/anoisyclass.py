from sys import exit
n = int(input())
in_deg = [0 for i in range(n)]
graph = [[] for i in range(n)]
visited = [False for i in range(n)]
count = 0

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    in_deg[b - 1] += 1

while True:
    found = False
    for i, v in enumerate(in_deg):
        if visited[i]:
            continue
        if v == 0:
            count += 1
            found = True
            visited[i] = True
            for ne in graph[i]:
                in_deg[ne] -= 1
            break
    if count == n:
        print("Y")
        exit(0)
    if not found:
        print("N")
        exit(0)