n, t = map(int, input().split())
cards = []
for i in range(n):
    name, cost = input().split()
    if int(cost) >= t - 1:
        continue
    cards.append((int(cost), name))
cards.sort()
hands = []
n = len(cards)
for i in range(n):
    first = cards[i]
    for j in range(i + 1, n):
        second = cards[j]
        left = t - first[0] - second[0]
        if left < 1:
            break
        for k in range(j + 1, n):
            if cards[k][0] <= left:
                third = cards[k]
                hand = sorted([first[1], second[1], third[1]])
                hands.append(hand)
hands.sort()
print("\n".join(" ".join(x) for x in hands))