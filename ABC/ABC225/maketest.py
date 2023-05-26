def f(i, j):
    return (i-1)*7 + j

def main():
    for i in range(1, 10):
        for j in range(1, 8):
            print(f(i, j), end = " ")
        print()

if __name__ == "__main__":
    main()