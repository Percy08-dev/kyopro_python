def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    res = [0 for _ in range(n)]
    x -= 1

    while res[x] != 1:
        res[x] = 1
        x = a[x]-1

    print(sum(res))

if __name__ == "__main__":
    main()