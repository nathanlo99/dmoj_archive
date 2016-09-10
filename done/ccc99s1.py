import sys


a = 0
b = 0
high = { "jack": 1, "queen": 2, "king": 3, "ace": 4 }

pile = [s.strip() for s in sys.stdin.read().split()]

for i, card in enumerate(pile):
    if card in high:
        if 52 - i > high[card] and all(x not in high for x in pile[i + 1:i + 1 + high[card]]):
            if i % 2 == 0:
                print("Player A scores {} point(s).".format(high[card]))
                a += high[card]
            else:
                print("Player B scores {} point(s).".format(high[card]))
                b += high[card]


print("Player A: {} point(s).".format(a))
print("Player B: {} point(s).".format(b))