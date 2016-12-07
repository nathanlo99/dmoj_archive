n = int(input())
m = int(input())

if n == 1 or m == 1 or (n + m) % 2 == 1:
    print("First")
else:
    print("Second")