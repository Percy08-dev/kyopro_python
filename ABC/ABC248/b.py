
def main():
    a, b, k = map(int, input().split())
    x = b/a
    cnt = 0
    while x > 1:
        x /= k
        cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()