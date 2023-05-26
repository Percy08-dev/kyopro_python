def f(a, b):
    return (4 * a * b) + (3 * a) + (3 * b)

def main():
    n = int(input())
    s = list(map(int, input().split()))
    board = set()

    for a in range(1, 1000):
        for b in range(1, 1000):
            m = f(a, b)
            if m > 1000:
                break
            board.add(m)

    print(sum([1 for i in s if not(i in board)]))

if __name__ == "__main__":
    main()