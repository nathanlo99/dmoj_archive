graph = {}
num_edges = 0

for i in range(4):
    for j, c in enumerate(input().split()):
        if c == "1":
            graph[i] = graph.get(i, []) + [j]
            if i <= j:
                num_edges += 1

if num_edges != 3:
    print("No")
else:
    for i in range(4):
        if i not in graph:
            others = [len(graph[x]) for x in graph if x != i]
            if min(others) == max(others):
                print("No")
                break
    else:
        print("Yes")