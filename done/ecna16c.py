s = input().strip()
k = input().strip()
d = ""

for i in range(len(k)):
    if i >= len(s):
        break
    c = chr((ord(s[i]) + 26 - ord(k[i])) % 26 + ord('A'))
    d += c
    
for i in range(len(k), len(s)):
    c = chr((ord(s[i]) + 26 - ord(d[-len(k)])) % 26 + ord('A'))
    d += c
print(d)