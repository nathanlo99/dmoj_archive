s = input().strip()

d = [set(), set(), set(), set()]

for i in range(0, len(s), 3):
    suit = s[i]
    num = int(s[i + 1:i + 3])
    cur = d["PKHT".index(suit)]
    if num in cur:
        print("GRESKA")
        break
    else:
        cur.add(num)
else:
    print(" ".join(map(str, (13 - len(j) for j in d))))