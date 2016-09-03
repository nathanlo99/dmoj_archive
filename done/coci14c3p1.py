keys = {
    "1QAZ": 0,
    "2WSX": 1,
    "3EDC": 2,
    "4RFV5TGB": 3,
    "6YHN7UJM": 4,
    "8IK,": 5,
    "9OL.": 6,
    "0P;/-['=]": 7
}

a = [0 for _ in keys]
for c in input():
    for key in keys:
        if c in key:
            a[keys[key]] += 1
            break
print("\n".join(map(str, a)))