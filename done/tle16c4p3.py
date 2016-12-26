import itertools
import sys

edges = set()
for _ in range(int(input())):
    a, b = map(int, input().split())
    edges.add((a, b))

for p in itertools.permutations(range(1, 9)):
    for a, b in ((1, 2), (2, 3), (3, 4), (4, 1), (5, 6), (6, 7), (7, 8), (8, 5), (1, 5), (2, 6), (3, 7), (4, 8)):
        if (p[a - 1], p[b - 1]) not in edges and (p[b - 1], p[a - 1]) not in edges:
            break
    else:
        print("Ja")
        sys.exit(0)
print("Nej")