def main():
    n, w = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: x[0], reverse = True)

    oishi = 0
    g = 0

    for i in data:
        if g + i[1] > w:
            tmp = w - g
            oishi += i[0] * tmp
            break
        oishi += i[0] * i[1]
        g += i[1]

    print(oishi)

if __name__ == "__main__":
    main()
