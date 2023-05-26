def main():
    q = int(input())

    s = []
    mem = 0
    f = False

    for _ in range(q):
        query = list(map(int, input().split(" ")))

        if query[0] == 1:
            s.append(query[1])
            f = len(s) > 1 and s[-1] < s[-2]
            
        elif query[0] == 2:
            print(s[mem])
            mem += 1
        else:
            if f:
                s = sorted(s[mem:])
                mem = 0
                f = False


main()