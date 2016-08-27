closest_vowel_ = " aae eei iiioo ooouu uuuuu"
next_consonant = " cdf ghj klmnp qrstv wxyzz"

for c in input():
    if c in "aeiou":
        print(c, end="")
    else:
        print("{}{}{}".format(c, closest_vowel_[ord(c) - ord('a')], next_consonant[ord(c) - ord('a')]), end="")
print()