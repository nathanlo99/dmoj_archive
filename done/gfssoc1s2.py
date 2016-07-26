replacements = {}
for i in range(int(input())):
    good, bad = input().split()
    replacements[bad] = good
for word in input().split():
    if word[-1] == ".":
        print(replacements.get(word[:-1], word[:-1]), end=".")
    else:
        print(replacements.get(word, word), end=" ")
