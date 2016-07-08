v = input()
n = input()
s = n[-1]
if s == "s":
    print(v + "-tu les", n, "?")
elif s == "e":
    print(v + "-tu la", n, "?")
else:
    print(v + "-tu le", n, "?")
