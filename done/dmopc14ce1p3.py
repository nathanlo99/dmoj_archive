import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bonds = []
num_bonds = [0 for i in range(n + 1)]
atoms = [None for i in range(n + 1)]
num_c = 0
num_h = 0

for _ in range(m):
    a, b = map(int, input().split())
    num_bonds[a] += 1
    num_bonds[b] += 1
    bonds.append((a, b))

for atom in range(1, n + 1):
    if num_bonds[atom] == 4:
        atoms[atom] = "C"
        num_c += 1
    elif num_bonds[atom] == 1:
        atoms[atom] = "H"
        num_h += 1
    else:
        print("Impossible")
        sys.exit(0)

energy = 0
done = set()
for atom1, atom2 in bonds:
    a1 = atoms[atom1]
    a2 = atoms[atom2]
    if a1 == "H":
        a1, a2 = a2, a1
    if a2 == "H":
        energy += 413
    elif a2 == "C":
        energy += 346
    if (atom1, atom2) in done:
        energy -= 2 * 346 - 615
    done.add((atom1, atom2))
print(energy)
line = "C"
if num_c > 1:
    line += str(num_c)
line += "H"
if num_h > 1:
    line += str(num_h)
print(line)