import sys
input = sys.stdin.readline

n, m, b, num_queries = map(int, input().split())
graph = [{} for i in xrange(n)]

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x - 1][y - 1] = z
    graph[y - 1][x - 1] = z

q = set(xrange(n))
dist = [10000000000 for i in xrange(n)]
dist[b - 1] = 0

while q:
    min_i = -1
    min_v = None
    for i in q:
        if min_i == -1 or dist[i] < min_v:
            min_i = i
            min_v = dist[i]
    q.remove(min_i)
    for neighbour in graph[min_i]:
        alt = min_v + graph[min_i][neighbour]
        if alt < dist[neighbour]:
            dist[neighbour] = alt

for i in xrange(num_queries):
    ans = dist[int(input()) - 1]
    if ans == 10000000000:
        print(-1)
    else:
        print(ans)