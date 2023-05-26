def main():
    n = int(input())
    cnt = 0

    for i in range(1, n):
        m = n//i
        if i**3 > n:
            break
        for j in range(i, n):
            d = m//j -j + 1
            if d <= 0:
                break
            cnt += d

    if n == 1:
        print(1)
    else:
        print(cnt)

if __name__ == "__main__":
    main()