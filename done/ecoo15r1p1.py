for i in range(10):
    count = {}
    s = input()
    time = 0
    while s != "end of box":
        count[s] = count.get(s, 0) + 1
        s = input()
    for color in count.keys():
        if color == "red":
            time += 16 * count["red"]
        else:
            while count[color] > 0:
                count[color] -= 7
                time += 13
    
    print(time)