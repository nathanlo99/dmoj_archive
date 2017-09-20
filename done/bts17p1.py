s = input().split()
ans = ""
for i, word in enumerate(s):
    if word[0].isupper() and i != 0:
        ans += "."
    ans += " " + word
print(ans + ".")