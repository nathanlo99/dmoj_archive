for _ in range(10):
    w = int(input())
    words = input().split()
    wp = 0
    cp = 0
    while wp < len(words):
        if cp + len(words[wp]) > w:
            print()
            cp = 0
        while len(words[wp]) > w:
            print(words[wp][:w])
            words[wp] = words[wp][w:]
        print(words[wp], end=" ")
        cp += len(words[wp]) + 1
        wp += 1
    print()        
    print("=====")