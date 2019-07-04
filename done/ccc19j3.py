for _ in range(int(input())):
    s = input()
    
    cnt = 1
    sym = s[0]
    
    line = ""
    for c in s[1:]:
        if c == sym:
            cnt += 1
        else:
            line += str(cnt) + " " + sym + " "
            cnt = 1
            sym = c
    
    if cnt > 0:
        line += str(cnt) + " " + sym
    else:
        line = line[:-2]
    print(line)