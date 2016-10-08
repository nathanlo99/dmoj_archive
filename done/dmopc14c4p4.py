import sys
input = sys.stdin.readline

s = input().strip()
candidates = set()
for i in xrange(len(s) - 8):
    if s[i] == s[i + 4] and s[i + 1] == s[i + 8]:
        candidates.add(i)

if len(candidates) == 0:
    print("KeyNotFoundError")
    sys.exit(0)
    
for i in xrange(int(input())):
    m = input().strip()
    for c in candidates:
        if all(s[c + i] == m[ch] for i, ch in ((0, 7), (1, 0), (2, 8), (3, 11), (5, 24), (6, 3), (7, 17))):
            back = {}
            for i, ch in enumerate(m):
                back[ch] = chr(ord("A") + i)
            print("".join(back[i] for i in s))
            sys.exit(0)

print("KeyNotFoundError")