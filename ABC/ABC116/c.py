def main():
    n = int(input())
    h = list(map(int,input().split()))
    cnt = 0

    while sum(h) != 0:
        p = 0
        while p < n:
            if h[p] > 0:
                cnt += 1
            while p < n and h[p] > 0:
                h[p] -= 1
                p += 1
            p += 1

    print(cnt)


if __name__ == "__main__":
    main()