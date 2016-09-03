input()
xyene = map(int, input().split())
fatal = map(int, input().split())
xp, fp = 0, 0
for x, f in zip(xyene, fatal):
    if x > f:
        xp += 1
    elif f > x:
        fp += 1
print("{} {}".format(xp, fp))
if xp == fp:
    print("Tie")
elif xp > fp:
    print("Xyene")
else:
    print("FatalEagle")