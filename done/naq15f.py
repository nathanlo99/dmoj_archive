for _ in range(int(input())):
    d = set()
    ans = ""
    for i in input():
        d.add(i)
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in d and i.upper() not in d:
            ans += i
    if ans == "":
        print("pangram")
    else:
        print("missing " + ans)