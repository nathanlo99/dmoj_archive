a, b = 0, 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    a = max(a, x * y)
for _ in range(int(input())):
    x, y = map(int, input().split())
    b = max(b, x * y)
if a > b:
    print("Casper")
elif a == b:
    print("Tie")
else:
    print("Natalie")