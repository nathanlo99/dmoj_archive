import sys
input = sys.stdin.readline
input()
bottom = []
top = []
for i, c in enumerate(input().strip()):
    if c == "0":
        bottom.append(i + 1)
    else:
        top.append(i + 1)
sandwich = top[::-1] + bottom
print("\n".join(str(x) for x in sandwich))