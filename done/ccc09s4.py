import sys
import heapq
input = sys.stdin.readline

n = int(input())
t = int(input())

stores = [-1 for i in xrange(1 + n)]
neighbours = [[] for i in xrange(1 + n)]
roads = [[-1 for i in xrange(1 + n)] for j in xrange(1 + n)]

for i in xrange(t):
    x, y, c = map(int, input().split())
    roads[x][y] = c
    roads[y][x] = c
    neighbours[x].append(y)
    neighbours[y].append(x)
    
for i in xrange(int(input())):
    z, c = map(int, input().split())
    stores[z] = c

d = int(input())

distance = [10000000 for i in xrange(n + 1)]
distance[d] = 0

q = [(0, d)]
for i in xrange(1, n + 1):
    if i != d:
        q.append((distance[i], i))

num_stores = len(stores)
min_dist = 10000000
while q:
    min_v, min_i = heapq.heappop(q)
    if min_v > min_dist:
        break
    for dest in neighbours[min_i]:
        alt = min_v + roads[min_i][dest]
        if alt < distance[dest]:
            distance[dest] = alt
            heapq.heappush(q, (alt, dest))
    if stores[min_i] != -1:
        min_dist = min(min_dist, min_v + stores[min_i])
        num_stores -= 1
        if num_stores == 0:
            break

print(min_dist)