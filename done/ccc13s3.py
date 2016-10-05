t = int(input()) - 1
g = int(input())

scores = [0, 0, 0, 0]
games = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

def recurse(index, score):
    if index == len(games):
        return 1 if (score.index(max(score)) == t and score.count(max(score)) == 1) else 0
    res = 0
    a, b = games[index]
    new_score = list(score)
    new_score[a] += 3
    res += recurse(index + 1, new_score)

    new_score = list(score)
    new_score[a] += 1
    new_score[b] += 1
    res += recurse(index + 1, new_score)

    new_score = list(score)
    new_score[b] += 3
    res += recurse(index + 1, new_score)
    return res

for i in range(g):
    a, b, sa, sb = map(int, input().split())
    a -= 1
    b -= 1
    games.remove((a, b))
    if sa == sb:
        scores[a] += 1
        scores[b] += 1
    elif sa > sb:
        scores[a] += 3
    else:
        scores[b] += 3

print(recurse(0, scores))