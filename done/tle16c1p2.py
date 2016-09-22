import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input().strip())
nums = sorted(int(input().strip()) for i in range(n))

mean = sum(nums) / float(n)
median = (nums[n // 2] + nums[n // 2 - 1]) / 2.0 if n % 2 == 0 else nums[n // 2]

d = defaultdict(int)
for num in nums:
    d[num] += 1
    
max_ = max(d.values())
f = [num for num in nums if d[num] == max_]
mode = sum(f) / float(len(f))

avg = min(mean, median, mode)

ans = 0
while nums[ans] <= avg:
    ans += 1
print(ans)