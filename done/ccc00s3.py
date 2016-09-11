import re
from sys import exit

link_graph = {}
link_regex = re.compile("<A HREF=\"([^\"]*)\">")

for i in range(int(input())):
    current_url = input()
    page = ""
    s = input()
    while "</HTML>" not in s:
        page += s
        s = input()
    for dest in re.findall(link_regex, page):
        link_graph[current_url] = link_graph.get(current_url, []) + [dest]
        print("Link from {} to {}".format(current_url, dest))
print()
while True:
    source = input()
    try:
        dest = input()
    except EOFError:
        exit(0)
    # Calculate from source to dest
    if source not in link_graph:
        print("Can't surf from {} to {}".format(source, dest))
        continue
    visited = [source]
    q = [source]
    done = False
    while q:
        node = q[0]
        q = q[1:]
        for neighbour in link_graph[node]:
            if neighbour == dest:
                done = True
                break
            if neighbour in visited or neighbour not in link_graph:
                continue
            visited.append(neighbour)
            q.append(neighbour)
        if done:
            break
    if dest in visited or done:
        print("Can surf from {} to {}".format(source, dest))
    else:
        print("Can't surf from {} to {}".format(source, dest))