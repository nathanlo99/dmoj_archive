def toRomanSymbol(n):
    if n > 1000:
        return "CONCORDIA CUM VERITATE"
    if n == 1000:
        return "M"

    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    hundred = n // 100
    n %= 100
    ten = n // 10
    n %= 10
    one = n

    return hundreds[hundred] + tens[ten] + ones[one]


def toNumber(s):
    s += " "
    values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    next_c = {"I": "VX", "X": "LC", "C": "DM"}
    result = 0
    for i, c in enumerate(s):
        if c == " ":
            continue
        if s[i + 1] in next_c.get(c, ""):
            result -= values[c]
        else:
            result += values[c]
    return result

for i in range(int(input())):
    s = input()
    a, b = s[:-1].split("+")
    print(a + "+" + b + "=" + toRomanSymbol(toNumber(a) + toNumber(b)))
