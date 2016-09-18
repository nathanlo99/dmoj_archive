import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
ab = zip([input().strip() for i in range(n)], [input().strip() for i in range(n)])

def solve(aa, bb, nn, m):
    if aa == bb and aa != "":
        return m
    if nn == 0:
        return None
    if not (aa.startswith(bb) or bb.startswith(aa)):
        return None

    for i, (a, b) in enumerate(ab):
        mm = solve(aa + a, bb + b, nn - 1, m + [i + 1])
        if mm:
            return mm
    return None

mm = solve("", "", m, [])
if mm:
    print(len(mm))
    for k in mm:
        print(k)
else:
    print("No solution.")