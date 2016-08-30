s = input().split(":")
seg = int(s[0], 16)
off = int(s[1], 16)

tot = seg * 16 + off
for off in range(off % 16, off % 16 + 0xFFFF, 16):
    seg = ((tot - off) // 16) & 0xFFFF
    print("{:04X}:{:04X}".format(seg, off & 0xFFFF))