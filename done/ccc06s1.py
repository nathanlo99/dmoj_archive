a = input()
b = input()

def to_generic_genome(genome):
    return "".join(map(lambda c: "a" if ord(c) >= ord("a") else "A", genome))

for i in range(int(input())):
    c = input()
    for j in range(5):
        a_gen = to_generic_genome(a[2 * j: 2 * j + 2])
        b_gen = to_generic_genome(b[2 * j: 2 * j + 2])
        c_gen = "a" if ord(c[j]) >= ord("a") else "A"
        if (a_gen == "AA" or b_gen == "AA") and c_gen == "a":
            print("Not their baby!")
            break
        elif a_gen == "aa" and b_gen == "aa" and c_gen == "A":
            print("Not their baby!")
            break
    else:
        print("Possible baby.")