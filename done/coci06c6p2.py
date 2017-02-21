import sys
input = sys.stdin.readline
r, c = map(int, input().split())
s = [input() for _ in range(r)]
a, b = map(int, input().split())

for i in range(2 * r):
    line = ""
    for j in range(2 * c):
        if i >= r: x = 2 * r - i - 1
        else: x = i
        if j >= c: y = 2 * c - j - 1
        else: y = j
        char = s[x][y]
        if (i, j) == (a - 1, b - 1):
            char = {"#": ".", ".": "#"} [char]
        line += char
    print(line)