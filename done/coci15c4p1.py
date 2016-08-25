a = input()
b = input()
if len(a) > len(b):
    b = "0" * (len(a) - len(b)) + b
elif len(b) > len(a):
    a = "0" * (len(b) - len(a)) + a
ar = ""
br = ""
for ac, bc in zip(a, b):
    if ac > bc:
        ar += ac
    elif ac < bc:
        br += bc
    else:
        ar += ac
        br += bc

if ar != "":
    print(int(ar))
else:
    print("YODA")
if br != "":
    print(int(br))
else:
    print("YODA")