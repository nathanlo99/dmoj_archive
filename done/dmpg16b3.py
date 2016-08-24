s = []
for i in range(3):
    s.append(input())
v, h, w = map(int, input().split())

total_width = 1 + w + 3 + w + 1
print("=" * total_width)
value_width = 4 if v == 1000 else 3
print("|" + str(v) + " " * (total_width - 2 - value_width) + "|")
for i in range(h - 1):
    print("|" + " " * (total_width - 2) + "|")
for i in range(3):
    print("|" + " " * w + s[i] + " " * w + "|")
for i in range(h - 1):
    print("|" + " " * (total_width - 2) + "|")
print("|" + " " * (total_width - 2 - value_width) + str(v) + "|")
print("=" * total_width)