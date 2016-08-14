n = input()
b = list("BFTCL")
for k in n:
    if k in b:
        b.remove(k)
if b:
    print("\n".join(b))
else:
    print("NO MISSING PARTS")
