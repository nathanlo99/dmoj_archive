import sys
input = sys.stdin.readline

nums = sorted(int(input()) for _ in xrange(int(input())))
p = 0
ans = 1
m = False

while p + 1 < len(nums) and nums[p + 1] < 0:
    ans *= nums[p] * nums[p + 1]
    p += 2
    m = True

o = []

if p < len(nums):
    if nums[p] < 0:
        p += 1
    else:
        o.append(nums[p])

while p < len(nums):
    if nums[p] >= 2:
        ans *= nums[p]
        m = True
    else:
        o.append(nums[p])
    p += 1

if m:
    print(ans)
elif o != []:
    print(max(o))
else:
    print(nums[-1])