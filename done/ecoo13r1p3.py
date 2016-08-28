import sys
input = sys.stdin.readline

for _ in range(10):
    rows = [[] for i in range(16)]
    cols = [[] for i in range(16)]
    cels = [[] for i in range(16)]
    solved = 0
    for row in range(16):
        s = input().strip()
        for col, value in enumerate(s):
            rows[row].append(value)
            cols[col].append(value)
            cels[(row // 4) * 4 + (col // 4)].append(value)

    for row in range(16):
        for col in range(16):
            if rows[row][col] == "-":
                for poss in "0123456789ABCDEF":
                    if poss in rows[row] or poss in cols[col] or poss in cels[(row // 4) * 4 + (col // 4)]:
                        continue
                    else:
                        rows[row][col] = poss
                        cols[col][row] = poss
                        cels[(row // 4) * 4 + (col // 4)][(row % 4) * 4 + (col % 4)] = poss
                        solved += 1
                        break
    print(solved)