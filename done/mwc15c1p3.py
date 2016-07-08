from collections import Counter

input()
n = Counter(map(int, input().split()))
m = sorted(n.most_common(), key = lambda x: (x[1], x[0]), reverse=True)
print(abs(m[0][0] - m[-1][0]))
