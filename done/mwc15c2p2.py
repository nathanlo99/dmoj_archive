import sys
input = sys.stdin.readline

input()
stack = [(1000000, 0)]

ans = []
for index, tower in enumerate(map(int, input().split())):
    while tower >= stack[-1][0]:
        stack.pop()
    ans.append(index - stack[-1][1])
    stack.append((tower, index))
print(" ".join(map(str, ans)))