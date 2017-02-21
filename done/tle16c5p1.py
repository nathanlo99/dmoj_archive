words = input().split()
vowels = "aeiou"

for word in words:
    v, c = 0, 0
    if len(word) == 1 and word[0] not in vowels:
        print("not readable")
        break
    for char in word:
        if char in vowels:
            v += 1
        else:
            c += 1
    if not (-1 <= v - c <= 1 or (v, c) == (1, 0)):
        print("not readable")
        break
else:
    print("readable")