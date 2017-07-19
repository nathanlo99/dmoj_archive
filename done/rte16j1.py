s = "".join(input().split())

a = s.count("L")

b = 0
d = 0

for c in s:
    if c == "L":
        b += 1
        d = max(d, b)
    else:
        b = 0

print(a, d)