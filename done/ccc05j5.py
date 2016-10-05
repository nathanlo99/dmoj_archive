import sys
input = sys.stdin.readline

def monkey(s):
    if a_word(s):
        return True
    for i, c in enumerate(s):
        if c == "N":
            if a_word(s[:i]) and monkey(s[i + 1:]):
                return True
    return False

def a_word(s):
    if s == "A":
        return True
    if len(s) >= 1 and s[0] == "B" and s[-1] == "S" and monkey(s[1:-1]):
        return True
    return False

s = input().strip()
while s != "X":
    print("YES" if monkey(s) else "NO")
    s = input().strip()