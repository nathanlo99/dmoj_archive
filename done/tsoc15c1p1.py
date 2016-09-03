for _ in range(int(input())):
    f = True
    for c in input().split():
        if c not in ["Cl", "Br", "Xe", "Kr", "Si", "As", "Rn", "Ne",
                     "He", "H", "C", "N", "O", "F", "P", "S", "I"]:
            f = False
            break
    if not f: print("Not molecular!")
    else: print("Molecular!")