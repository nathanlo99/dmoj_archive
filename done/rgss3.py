for _ in range(int(input())):
    substring = input().strip()
    string = input().strip()
    while True:
        if len(string) == len(substring):
            if string != substring:
                print("NO")
            else:
                print("YES")
            break
        if string[-1] == "A":
            string = string[:-1]
        else:
            string = string[:-1]
            string = string[::-1]