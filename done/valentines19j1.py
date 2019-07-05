for _ in range(int(input())):
    n = int(input())
    if n < 1000:
        print("Newbie")
    elif n <= 1199:
        print("Amateur")
    elif n <= 1499:
        print("Expert")
    elif n <= 1799:
        print("Candidate Master")
    elif n <= 2199:
        print("Master")
    elif n <= 2999:
        print("Grandmaster")
    elif n <= 3999:
        print("Target")
    else:
        print("Rainbow Master")