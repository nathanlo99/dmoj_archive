in_deg = [None, 1, 0, 0, 2, 1, 0, 1]
graph = {
    1: [4, 7],
    2: [1],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: []
}

x = int(input())
y = int(input())
while x != 0:
    in_deg[y] += 1
    graph[x].append(y)
    x = int(input())
    y = int(input())

done = []
while True:
    for i, v in enumerate(in_deg):
        if v == 0:
            in_deg[i] -= 1
            done.append(str(i))
            for n in graph[i]:
                in_deg[n] -= 1
            break
    else:
        if len(done) != 7:
            print("Cannot complete these tasks. Going to bed.")
        else:
            print(" ".join(done))
        break