transitions = (
    (1, 3, -1),
    (-1, 2, -1),
    (6, -1, 7),
    (5, -1, 4),
    (-1, -1, -1),
    (-1, 3, 4),
    (-1, 2, 7),
    (-1, -1, -1),
)

def next(s):
    if len(s) >= 2 and (s[:2] == "bd" or s[:2] == "ch"):
        return 0, 2
    if s[0] in "tmdbr":
        return 0, 1
    if len(s) >= 2 and s[:2] == "oo":
        return 1, 2
    if s[0] in "aei":
        return 1, 1
    if s[0] in "nvf":
        return 2, 1
    return 3, -1

words = raw_input().split()
if len(words) < 2:
    print("invalid")
else:
    for word in words:
        word = word.lower()
        state = 0
        while True:
            transition, length = next(word)
            word = word[length:]
            state = transitions[state][transition]
            if state == -1 or not word:
                break
        if state not in (4, 5, 6, 7):
            print("invalid")
            break
    else:
        print("valid")