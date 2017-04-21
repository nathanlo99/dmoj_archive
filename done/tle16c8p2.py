for _ in range(int(input())):
    a = int(input())
    for c in bin(a)[2:]:
        print("meme" if c == '0' else "dank", end=" ")
    print()