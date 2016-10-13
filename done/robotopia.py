import sys
input = sys.stdin.readline

for _ in xrange(int(input())):
    l1, a1, l2, a2, lt, at = map(int, input().split())
    ans = set()
    for x in xrange(1, 10000):
        legs = lt - l1 * x
        arms = at - a1 * x
        if legs % l2 == 0 and legs >= l2 and arms % a2 == 0 and arms >= a2 and legs // l2 == arms // a2:
            ans.add((x, legs // l2))
            if len(ans) > 1:
                break

    if len(ans) == 1:
        x, y = ans.pop()
        print x, y
    else:
        print "?"