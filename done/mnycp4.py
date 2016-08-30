import re
a = ["t", "m", "d", "b", "r"]
b = ["a", "e", "i"]
c = ["n", "v", "f"]

ending = [4, 5, 6, 7]
transitions = {
        0: {"A": 1, "B": 3},
        1: {"B": 2},
        2: {"A": 6, "C": 7},
        3: {"A": 5, "C": 4},
        4: {},
        5: {"B": 3, "C": 4},
        6: {"B": 2, "C": 7},
        7: {}
    }

def next(s):
    if len(s) >= 2 and (s[:2] == "bd" or s[:2] == "ch"):
        return "A", 2
    if s[0] in a:
        return "A", 1
    if len(s) >= 2 and s[:2] == "oo":
        return "B", 2
    if s[0] in b:
        return "B", 1
    if s[0] in c:
        return "C", 1
    return "ERROR", -1

invalid = False
words = input().split()
if len(words) < 2:
    print("invalid")
else:
    for word in words:
        word = word.lower()
        state = 0
        while word:
            transition, length = next(word)
            word = word[length:]
            if transition not in transitions[state]:
                invalid = True
                break
            state = transitions[state][transition]
        if invalid or state not in ending:
            print("invalid")
            break
    else:
        print("valid")