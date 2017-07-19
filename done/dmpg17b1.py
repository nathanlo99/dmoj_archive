"""
3
1 4
2 1
1 1
"""

s = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    # max b while min a
    s.append((-b, a))
b, a = min(s)
print(a, -b)