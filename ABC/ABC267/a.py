from operator import index


def main():
    s = input()
    L = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(5 - L.index(s))

if __name__ == "__main__":
    main()