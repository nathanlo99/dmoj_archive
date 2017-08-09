import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))

for i in range(4):
    for j in range(4):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print(" ".join(map(str, nums)))