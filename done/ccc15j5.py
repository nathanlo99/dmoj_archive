memo = {}
def solve(pieces, people, min_):
    if (pieces, people, min_) in memo:
        return memo[(pieces, people, min_)]
    if people == 1 or people == pieces:
        res = 1
    else:
        res = 0
        for p in range(min_, (pieces // people) + 1):
            res += solve(pieces - p, people - 1, p)
    memo[(pieces, people, min_)] = res
    return res

n = int(input())
k = int(input())
print(solve(n, k, 1))