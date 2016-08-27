n = int(input())
num = sorted(map(int, input().split()))
l, r = 0, n - 1
while l <= r:
    print("{} {} ".format(num[l], num[r]), end="")
    l += 1
    r -= 1