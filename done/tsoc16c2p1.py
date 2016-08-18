n = int(input())
types = []
count = 0
s = input()
for c in s:
    if c in "AOR":
        if count == 0:
            types.append(c)
        else:
            types[-count] = c
            count = 0
    else:
        count += 1
invitations = {
    "A": "Dear {}, beloved artist, I would love to have you at my party. Come to my crib on April 20th.",
    "O": "Dear {}, beloved occasion enthusiast, come to my crib to celebrate this very special day.",
    "R": "Dear {}, April 20th is happening again this year. Don't miss out."
}

for v in types:
    print(invitations[v].format(input()))
