input()
nums = sum(map(int, input().split()))
if nums > 200:
    print("Over maximum capacity!")
else:
    print(200 - nums)