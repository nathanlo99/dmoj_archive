l = []
while(True):
    n = input().split()
    l.append((int(n[1]), n[0]))
    if n[0] == "Waterloo":
        break
print(sorted(l)[0][1])
