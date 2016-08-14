graph = {1: [6], 2: [6], 3: [4, 5, 6, 15], 4: [3, 5, 6], 5: [3, 4, 6],
         6: [1, 2, 3, 4, 5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10, 12],
         10: [9, 11], 11: [10, 12], 12: [9, 11, 13], 13: [12, 14, 15],
         14: [13], 15: [3, 13], 16: [17, 18], 17: [16, 18], 18: [16, 17]}

while True:
    mode = input()
    if mode == "q":
        break

    elif mode == "i":
        x = int(input())
        y = int(input())
        if y not in graph.get(x, []):
            graph[x] = graph.get(x, []) + [y]
        if x not in graph.get(y, []):
            graph[y] = graph.get(y, []) + [x]

    elif mode == "d":
        x = int(input())
        y = int(input())
        graph[x].remove(y)
        graph[y].remove(x)
        if not graph[x]:
            graph.pop(x)
        if not graph[y]:
            graph.pop(y)

    elif mode == "n":
        x = int(input())
        print(len(graph.get(x, [])))

    elif mode == "f":
        x = int(input())
        total = []
        for friend in graph.get(x, []):
            total += graph.get(friend, [])
        print(len(set(t for t in total if t != x and t not in graph.get(x, []))))

    elif mode == "s":
        x = int(input())
        y = int(input())

        distance = {x: 0}

        q = [x]

        while(q):
            u = q[0]
            q = q[1:]
            for node in graph.get(u, []):
                if node in distance:
                    continue
                distance[node] = distance[u] + 1
                q.append(node)
        print(distance.get(y, "Not connected"))
