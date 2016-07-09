input()
towers = map(int, input().split())
height_stack = [1000000]
index_stack = [0]
views = []

for index, tower in enumerate(towers):
    while len(height_stack) > 0 and tower >= height_stack[-1]:
        height_stack.pop()
        index_stack.pop()
    views.append(index - index_stack[-1])
    height_stack.append(tower)
    index_stack.append(index)

print(" ".join(map(str, views)))
