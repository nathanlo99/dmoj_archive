griffy = False
timothy = False
d1, d2, c1, c2, c3 = 0, 0, 0, 0, 0

for i in range(3):
    s = input()
    if (s == "OOO"):
        griffy = True
    if (s == "XXX"):
        timothy = True
    c1 += 1 if s[0] == 'O' else 0
    c2 += 1 if s[1] == 'O' else 0
    c3 += 1 if s[2] == 'O' else 0
    d1 += 1 if s[i] == 'O' else 0
    d2 += 1 if s[2 - i] == 'O' else 0
if (c1 == 3):
    griffy = True
if (c2 == 3):
    griffy = True
if (c3 == 3):
    griffy = True
if (c1 == 0):
    timothy = True
if (c2 == 0):
    timothy = True
if (c3 == 0):
    timothy = True
if (d1 == 3):
    griffy = True
if (d1 == 0):
    timothy = True
if (d2 == 3):
    griffy = True
if (d2 == 0):
    timothy = True

if griffy and timothy:
    print("Error, redo")
elif griffy:
    print("Griffy")
elif timothy:
    print("Timothy")
else:
    print("Tie")
