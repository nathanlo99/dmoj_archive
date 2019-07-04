a = input().replace(" ", "")
b = input().replace(" ", "")
print("Is an anagram." if set(a) == set(b) else "Is not an anagram.")