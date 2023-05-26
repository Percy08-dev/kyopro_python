def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        # v, w, x, y, z = map(int, input().split())
        if sum(map(int, input().split())) < 20:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()