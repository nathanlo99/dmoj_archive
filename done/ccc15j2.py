n = input()
h = n.count(":-)")
s = n.count(":-(")
if h > s:
    print("happy")
elif h < s:
    print("sad")
elif h == 0:
    print("none")
else:
    print("unsure")
