import bisect

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[::-1]
    b = list(map(int, input().split()))[::-1]
    ans = 0

    for i in range(n):
        # Left-most element of b that is >= a[i]
        m = bisect.bisect_left(b, a[i])
        ans = max(ans, i - m)
    print("The maximum distance is {}".format(ans))