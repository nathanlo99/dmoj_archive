m = {"A": [1, 0, 2], "B": [0, 2, 1], "C": [2, 1, 0]}
b = 0
for c in input():
    b = m[c][b]
print(b + 1)