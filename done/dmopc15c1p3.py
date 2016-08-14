a = input()
b = input()


def check(a, shift, b):
    for i in range(len(a)):
        if chr((ord(a[i]) - ord('a') - shift) % 26 + ord('a')) != b[i]:
            return False
    return True

MIN = 26

for i in range(len(a) - len(b) + 1):
    for j in range(MIN):
        if check(a[i:i + len(b)], j, b):
            MIN = j

print(MIN)
print("".join(chr((ord(i) - ord('a') - MIN) % 26 + ord('a')) for i in a))
