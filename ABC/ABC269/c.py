def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

def main():
    n = int(input())
    nb = [n >> i & 1 == 1 for i in range(60)]
    popnum = popcnt(n)

    for bit in range(2**popnum):
        shift = 0
        num = 0
        for i in range(60):
            if nb[i]:
                if bit >> shift & 1 == 1:
                    num += 1 << i
                shift += 1
        print(num)



if __name__ == "__main__":
    main()