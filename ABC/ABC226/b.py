def main():
    x = int(input())
    data = set()
    for _ in range(x):
        L = input()
        data.add(L)

    print(len(data))


if __name__ == "__main__":
    main()