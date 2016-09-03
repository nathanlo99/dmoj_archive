n, k = map(int, input().split())
words = [c for c in input().split()[1:]]
for i in range(n - 1):
    last_words = [word for word in words]
    for c in input().split()[1:]:
        for word in last_words:
            if len(word) + 1 <= k:
                words.append(word + c)

print("\n".join(sorted(words)))