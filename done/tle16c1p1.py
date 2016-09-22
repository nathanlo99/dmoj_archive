input()
d = list(map(int, input().split()))
da, db = min(d), max(d)
input()
q = list(map(int, input().split()))
qa, qb = min(q), max(q)

if db * 5 < qa * 2:
    print("Dimes are better")
elif da * 5 > qb * 2:
    print("Quarters are better")
else:
    print("Neither coin is better")