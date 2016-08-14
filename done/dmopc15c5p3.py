E, N = map(int, input().split())
nums = map(int, input().split()[::-1] + [str(E)])

cur = 10
for num in nums:
    if cur == 1:
        cur = len(str(num))
    else:
        cur = int(str(num),  cur)

print(cur)
