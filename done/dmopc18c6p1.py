input()
s = input()
letters = set(s)

if not letters.issubset(set("ACTGU")) or set("TU").issubset(letters):
    print("neither")
elif "T" in letters:
    print("DNA")
elif "U" in letters:
    print("RNA")
else:
    print("both")