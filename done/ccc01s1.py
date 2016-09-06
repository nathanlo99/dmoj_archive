current_suit = ""
suits = "CDHS"
cards = {}
scores = {}
score = {"A": 4, "K": 3, "Q": 2, "J": 1}

for c in input():
    if c in suits:
        current_suit = c
    elif current_suit in cards:
        cards[current_suit].append(c)
    else:
        cards[current_suit] = [c]
    scores[current_suit] = scores.get(current_suit, 0) + score.get(c, 0)

for suit in suits:
    if suit not in cards:
        scores[suit] = 3
    elif len(cards[suit]) == 1:
        scores[suit] += 2
    elif len(cards[suit]) == 2:
        scores[suit] += 1

print("Cards Dealt Points")
print("Clubs " + " ".join(cards.get("C", [])) + " " + str(scores["C"]))
print("Diamonds " + " ".join(cards.get("D", [])) + " " + str(scores["D"]))
print("Hearts " + " ".join(cards.get("H", [])) + " " + str(scores["H"]))
print("Spades " + " ".join(cards.get("S", [])) + " " + str(scores["S"]))
print("Total " + str(sum(scores.values())))