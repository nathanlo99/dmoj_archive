import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n)]
prob = [0.0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
prob[0] = 1.0
for i in range(n):
    if len(graph[i]) != 0:
        temp = prob[i] / len(graph[i])
        for neighbour in graph[i]:
            prob[neighbour] += temp
    else:
        print(prob[i])
