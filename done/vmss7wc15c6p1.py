count = [0 for _ in range(26)]
for c in input():
    if c != ' ': count[(ord(c) - min(ord('A'), ord('a'))) % 32] += 1
for c in input():
    if c != ' ': count[(ord(c) - min(ord('A'), ord('a'))) % 32] -= 1
print("yes" if all(x == 0 for x in count) else "no")