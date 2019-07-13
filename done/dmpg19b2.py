a = list(map(int, input().split()))

m = max(a)
mi = a.index(m)
a[mi] = 0
n = max(a)
ni = a.index(n)

if (mi, ni) in ((0, 2), (2, 0), (1, 3), (3, 1)):
    print("trans")
else:
    print("cis")