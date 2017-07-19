for _ in range(int(input())):
    s = input()
    line = ""
    lower = True
    for c in s:
        if c.isalpha():
            if lower:
                line += c.lower()
            else:
                line += c.upper()
            lower = not lower
        else:
            line += c
    print(line)