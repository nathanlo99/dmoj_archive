import sys

N, M = map(int, input().split())

graph = {}

for _ in range(M):
	a, b = map(int, input().split())
	graph[a] = graph.get(a, []) + [b]
	graph[b] = graph.get(b, []) + [a]

for a in range(1, N + 1):
	for b in graph.get(a, []):
		if b == a: continue
		for c in graph.get(b, []):
			if c in [a, b]: continue
			for d in graph.get(c, []):
				if d in [a, b, c]: continue
				for e in graph.get(d, []):
					if e in [a, b, c, d]: continue
					for f in graph.get(e, []):
						if f in [a, b, c, d, e]: continue
						for g in graph[f]:
							if g == a and g not in [b, c, d, e, f]:
								print("YES")
								sys.exit(0)
print("NO")
