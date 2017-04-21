s = set(input())
for _ in range(int(input())):
    a = set(input())
    if a.issuperset(s):
        print("yes")
    else:
        print("no")