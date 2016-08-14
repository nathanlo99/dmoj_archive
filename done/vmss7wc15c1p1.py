n = input()
a = sum(map(int, list(n[0:3])))
b = sum(map(int, list(n[4:7])))
c = sum(map(int, list(n[8:])))
if a == b == c:
    print("Goony!")
else:
    print("Pick up the phone!")
