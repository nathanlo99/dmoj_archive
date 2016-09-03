n = int(input())
original = ["GGGGG", "G....", "G..GG", "G...G", "GGGGG"]
for i in range(5 * n):
    for j in range(5 * n):
        print(original[i // n][j // n], end="")
    print()