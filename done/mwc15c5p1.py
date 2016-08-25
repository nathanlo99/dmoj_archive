n = int(input())
counts = {}
scores = sorted(map(float, input().split()))
for score in scores:
    counts[score] = counts.get(score, 0) + 1
    
if n % 2 == 0:
    median = (scores[n // 2 - 1] + scores[n // 2]) / 2.0
else:
    median = scores[n // 2]

highest_freq = max(counts.values())
modes = sorted(i for i in counts.keys() if counts[i] == highest_freq)
print(sum(scores) / float(n))
print(median)
print(" ".join(map(str, modes)))