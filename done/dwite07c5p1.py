for _ in range(5):
    n = int(input())
    print("".join(" ~.~ " for __ in range(n)))
    print("".join("`   `" for __ in range(n)))
    print("".join(" \./ " for __ in range(n)))