s = input()
scores = []
for i in range(4):
    score, full, weight = input().split()
    scores.append((int(score) * 100, int(full), float(weight)))
scores.sort(key=lambda x: x[-1], reverse=True)
if s == "trees!": scores[0] = (scores[0][1] * 100, scores[0][1], scores[0][2])
else: scores[0] = (0, scores[0][1], scores[0][2])
final = sum(x[0] / x[1] * x[2] for x in scores)
if final % 1 >= 0.5: print(int(final // 1 + 1))
else: print(int(final // 1))