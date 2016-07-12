words = [[] for i in range(26)]
for i in range(int(input())):
    s = input()
    words[ord(s[0]) - ord('a')].append(s)
for i in range(26):
    if words[i] != []:
        print(", ".join(sorted(words[i])))
