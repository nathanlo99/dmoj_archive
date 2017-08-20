for _ in range(10):
    k = int(input()) % 26
    s = input()
    if " " in s:
        # encode
        words = s.split()
        num = len(words)
        prefix = chr(ord("a") + num // 26) + chr(ord("a") + num % 26)
        for word in words:
            prefix += chr(ord("a") + len(word))
        word = prefix + "".join(words)
        n = 0
        ans = ""
        for c in word[::-1]:
            cc = ord(c) - ord("a")
            n += cc
            ans += chr(ord("a") + (n + k) % 26)
        print(ans[::-1])
    else:
        # decode
        letters = []
        for c in s:
            letters.append((ord(c) - ord("a") - k + 26) % 26)
        n = 0
        word = ""
        for c in letters[::-1]:
            cc = (c - n + 26) % 26
            n += cc
            word += chr(ord("a") + cc)
        word = word[::-1]
        num = (ord(word[0]) - ord("a")) * 26 + (ord(word[1]) - ord("a"))
        lengths = []
        for i in range(2, num + 2):
            lengths.append(ord(word[i]) - ord("a"))
        word = word[num + 2:]
        ans = ""
        lp = 0
        ln = 0
        for c in word:
            ans += c
            ln += 1
            if ln == lengths[lp]:
                lp += 1
                ln = 0
                ans += " "
        print(ans)