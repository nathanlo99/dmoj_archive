for i in range(10):
    if input() == "encode":
        words = input().split()
        l = [len(x) for x in words]
        p, lc, lp, s = 0, 0, 0, ""
        while p <= max(l):
            for word in words:
                if p < len(word):
                    s += word[p]
                    lc += 1
                    if lc == l[lp]:
                        s += " "
                        lc = 0
                        lp += 1
            p += 1
        print(s)
    else:
        words = input().split()
        l = [len(x) for x in words]
        p = ["" for x in words]
        letters = "".join(words)
        c = 0
        i = 0
        d = 0
        while d < len(l):
            if len(p[i]) < l[i]:
                p[i] += letters[c]
                c += 1
                if len(p[i]) == l[i]:
                    d += 1
            i += 1
            if i == len(l):
                i = 0
        print(" ".join(p))