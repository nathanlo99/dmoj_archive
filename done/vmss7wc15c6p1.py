count = [0 for _ in range(26)]
for c in input():
    if c != ' ': count[(ord(c) - min(ord('A'), ord('a'))) % 32] += 1
for c in input():
    if c != ' ': count[(ord(c) - min(ord('A'), ord('a'))) % 32] -= 1
print("yes" if max(count) == min(count) and min(count) == 0 else "no")