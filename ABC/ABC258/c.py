def main():
    n, q = map(int, input().split())
    s = input()

    p = 0

    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            p = (p-x)%n
        else:
            print(s[(p+x-1)%n])



if __name__ == "__main__":
    main()