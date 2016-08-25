s = input()
last_value = 0
last_base = 0

roman = { "I": 1, "V": 5,
          "X": 10, "L": 50,
          "C": 100, "D": 500,
          "M": 1000 }

ans = 0

for i in range(0, len(s), 2):
    base = roman[s[i + 1]]
    value = int(s[i]) * base
    if base > last_base:
        ans -= 2 * last_value
    ans += value
    last_value = value
    last_base = base
print(ans)