scores = []
for i in range(int(input())):
    s = list(map(int, input().split()))
    c = 1
    for j in range(1, len(s)):
        c *= s[j]
    scores.append((c, i + 1))
print("\n".join(map(str, (s[1] for s in sorted(scores, reverse=True)[:3]))))
