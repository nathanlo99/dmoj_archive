s = input()
strings = [""]
for i, c in enumerate(s[:-1]):
    strings[0] += c * (i + 1)
strings[0] += (s[-1] * len(s)) + strings[0][::-1]
print(strings[0])
for i in range(1, len(s) ** 2 // 2):
    strings.append(strings[i - 1][:i] + s[0] + strings[i - 1]
                   [i + 1:-i - 1] + s[0] + strings[i - 1][-i:])
    print(strings[-1])
print(s[0] * len(strings[0]))
print("\n".join(strings)[::-1])
