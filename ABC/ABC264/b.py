
def f(r, c):
    r = abs(r - 8)
    c = abs(c - 8)
    d = max(r, c)

    if d % 2 == 1:
        print("black")
    else:
        print("white")


def f1(r, c):
    r = abs(r - 8)
    c = abs(c - 8)
    d = max(r, c)

    if d % 2 == 1:
        print("■", end="")
    else:
        print("□", end="")


def main():
    r, c = map(int, input().split())
    f(r, c)

def test():
    for i in range(1, 16):
        for j in range(1, 16):
            f1(i, j)
        print()

if __name__ == "__main__":
    main()
    # test()