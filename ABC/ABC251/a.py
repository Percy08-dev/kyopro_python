def main():
    s = input()
    cnt = 0
    while cnt < 6:
        print(s, end="")
        cnt += len(s)

    print()

if __name__ == "__main__":
    main()