line = [0]
for _ in range(int(input())):
    line.append(int(input()))
line.append(0)

print(sum(1 for i in range(1, len(line) - 1) if max([line[i], line[i-1], line[i+1]]) < 41))
