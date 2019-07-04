n, m = map(int, input().split())
ai = list(map(int, input().split()))

for i in range(m):
    shortest = ai[0]
    shortest_idx = 0
    for idx, line in enumerate(ai[1:]):
        if line < shortest:
            shortest_idx = idx + 1
            shortest = line
    print(shortest)
    ai[shortest_idx] += 1