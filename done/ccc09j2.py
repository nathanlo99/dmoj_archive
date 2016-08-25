a = int(input())
b = int(input())
c = int(input())
n = int(input())

ans = 0
s = "{} Brown Trout, {} Northern Pike, {} Yellow Pickerel"
for i in range(n // a + 1):
    left = n - i * a
    for j in range(left // b + 1):
        still_left = left - j * b
        for k in range(still_left // c + 1):
            if i > 0 or j > 0 or k > 0:
                ans += 1
                print(s.format(i, j, k))
print("Number of ways to catch fish: {}".format(ans))