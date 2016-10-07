import sys
input = sys.stdin.readline

n = int(input())
children = [[]]

for i in range(n):
    children.append(list(map(int, input().split()))[1:])

mapping = [-1 for i in xrange(n + 1)]
def dfs1(node, num):
    mapping[node] = num
    diff = 1
    for i in children[node][::-1]:
        diff += dfs1(i, num + diff)
    return diff

def dfs2(node):
    s = [mapping[node]]
    for child in sorted(children[node], key=lambda x: mapping[x], reverse=True):
        s += dfs2(child)
    return s

dfs1(1, 1)
print(" ".join(map(str, dfs2(1))))