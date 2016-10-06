def left(s, i):
    if s[i] == ")":
        c = 1
        i -= 1
        while c > 0:
            if s[i] == ")":
                c += 1
            elif s[i] == "(":
                c -= 1
            if c == 0:
                break
            i -= 1
        s = s[:i] + ["("] + s[i:]
    else:
        s = s[:i] + ["("] + s[i:]
    return s

def right(s, i):
    if s[i] == "(":
        i += 1
        c = 1
        while c > 0:
            if s[i] == "(":
                c += 1
            elif s[i] == ")":
                c -= 1
            if c == 0:
                break
            i += 1
    s = s[:i + 1] + [")"] + s[i + 1:]
    return s

for _ in range(int(input())):
    s = input().split()
    i = 0
    while i < len(s):
        if s[i] == "X":
            s = left(s, i - 1)
            i += 1
            s = right(s, i + 1)
        i += 1
    i = 0
    while i < len(s):
        if s[i] in "+-":
            s = left(s, i - 1)
            i += 1
            s = right(s, i + 1)
        i += 1
    if s[0] == "(" and s[-1] == ")":
        s = s[1:-1]
    ans = ""
    last = "("
    for elem in s:
        if elem == "(" and last == "(":
            ans += "("
        elif elem == "(":
            ans += " ("
        elif elem == ")" and last == ")":
            ans += ")"
        elif elem == ")":
            ans += ")"
        elif last == "(":
            ans += elem
        else:
            ans += " " + elem
        last = elem
    print(ans)