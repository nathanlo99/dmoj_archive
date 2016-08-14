s = []
for i in range(int(input())):
    s.append(input())
if "Bayview" not in s or "Leslie" not in s:
    print("N")
else:
    b = s.index("Bayview")
    l = s.index("Leslie")
    if b == -1 or l == -1 or (b - l != 2 and l - b != 2) or s[(b + l) // 2] != "Bessarion":
        print("N")
    else:
        print("Y")
