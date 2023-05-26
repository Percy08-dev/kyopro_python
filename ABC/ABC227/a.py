def main():
    n, k, a = map(int, input().split())
    num = a
    k-=1
    while k > 0:
        num = (num)%(n) + 1
        k -= 1

    print(num)


if __name__ == "__main__":
    main()