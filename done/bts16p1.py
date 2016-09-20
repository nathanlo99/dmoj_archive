s = input()
lower, upper = 0, 0
for ch in s:
    if ord("a") <= ord(ch) <= ord("z"):
        lower += 1
    elif ord("A") <= ord(ch) <= ord("Z"):
        upper += 1
if lower > upper:
    print(s.lower())
elif upper > lower:
    print(s.upper())
else:
    print(s)