import sys
input = sys.stdin.readline

s = input().strip()
atoms = []
for ch in s:
    if ch in "CHO":
        atoms.append((ch, 0))
    else:
        prev_atom, prev_amt = atoms.pop()
        atoms.append((prev_atom, prev_amt * 10 + int(ch)))

compound = {"C": 0, "H": 0, "O": 0}
for atom, amt in atoms:
    compound[atom] += (1 if amt == 0 else amt)

c = 4 * compound["C"]
d = 2 * compound["H"]
b = c + compound["H"] - 2 * compound["O"]
a = 4

while a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
    a //= 2
    b //= 2
    c //= 2
    d //= 2

if min(a, b, c, d) <= 0:
    print("Impossible")
else:
    a, b, c, d = map(int, (a, b, c, d))
    print("{}{} + {}O2 -> {}CO2 + {}H2O".format(a, s, b, c, d))