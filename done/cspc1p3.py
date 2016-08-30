n = 1

while True:
    s = input()
    if s == "No More Words!":
        break
    if "ie" in s:
        i = s.index("ie")
        c = s[i - 1]
        if c == "c":
            print(s[:i] + "ei" + s[i + 2:])
        else:
            print("Word {} is correct.".format(n))
    if "ei" in s:
        i = s.index("ei")
        c = s[i - 1]
        if c != "c":
            print(s[:i] + "ie" + s[i + 2:])
        else:
            print("Word {} is correct.".format(n))
    n += 1