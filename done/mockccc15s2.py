from collections import Counter

d = {}
_ = input()
n = sorted(map(int, input().split()))
print(max(v for v in Counter(n).values()))
