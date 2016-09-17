memo = {}
def solve(s, i=0):
    if i in memo:
        return memo[i]
    ans = 0
    valid_ = False
    if i == len(s) - 1:
        return True, 0
    elif i >= len(s):
        return False, 0
    nums = ["ook", "ookook", "oog", "ooga", "ug", "mook", "mookmook",
                "oogam", "oogum", "ugug"]
    if s[i:] in nums:
        valid_ = True
        ans = 1
    for num in nums:
        if i + len(num) < len(s) and s[i:i+len(num)] == num:
            valid, count = solve(s, i + len(num))
            if valid:
                ans += count
                valid_ = True
    memo[i] = valid_, ans
    return valid_, ans

for _ in range(10):
    s = input()
    memo = {}
    print(solve(s)[1])