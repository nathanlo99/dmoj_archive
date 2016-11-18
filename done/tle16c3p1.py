from collections import defaultdict

n = int(input())
assert(1 <= n <= 20000)
words = defaultdict(int)
for i in range(n):
    word = input().strip()
    assert(1 <= len(word) <= 16)
    words[word] += 1
print(sum(1 for v in words.values() if v == 1))