for i in range(int(input())):
    value = int(input().strip(), 16)
    if (value >> 20) & 1 != 0:
        print("{:08X} ".format(value & ~(1 << 20)), end = "")
    print("{:08X}".format(value))