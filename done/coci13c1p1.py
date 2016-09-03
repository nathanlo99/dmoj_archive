c = {}

for i in range(int(input())):
    s = input()[0]
    c[s] = c.get(s, 0) + 1
five_or_more = [x for x in c if c.get(x, 0) >= 5]
if five_or_more == []:
    print("PREDAJA")
else:
    print("".join(map(str, sorted(five_or_more))))