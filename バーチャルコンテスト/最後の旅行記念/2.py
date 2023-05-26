def main():
    a, b, c = map(int, input().split())
    print(c if c < b//a else b//a)


if __name__ == "__main__":
    main()