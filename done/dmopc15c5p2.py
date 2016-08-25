names = ["Okabe", "Mayuri", "Daru", "Kurisu"]
taglines = ["elpsycongroo", "tuturu", "superhacker", "myfork"]

for i in range(int(input())):
    ptrs = [0, 0, 0, 0]
    s = input()
    for c in s:
        for j in range(4):
            if ptrs[j] < len(taglines[j]) and c == taglines[j][ptrs[j]]:
                ptrs[j] += 1
    candidates = []
    for j in range(4):
        if ptrs[j] == len(taglines[j]):
            candidates.append(names[j])
    if len(candidates) == 0:
        print("SERN spy!")
    else:
        print(" or ".join(candidates))