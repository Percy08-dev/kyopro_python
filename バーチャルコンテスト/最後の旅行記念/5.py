def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = sum(a)/n
    print(sum([i-x for i in a]))

    print()


if __name__ == "__main__":
    main()