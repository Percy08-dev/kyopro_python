def main():
    s = input()
    x = set(range(0, 10))

    for i in s:
        x.remove(int(i))

    print(x.pop())

if __name__ == "__main__":
    main()