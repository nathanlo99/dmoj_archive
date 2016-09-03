n = []
for _ in range(3):
    n.append(int(input()))
n.sort()
if n[0] + n[1] > n[2]: print("Huh? A triangle?")
else: print("Maybe I should go out to sea...")