def main():
    s = list(input())
    a = list("atcoder")

    ans = 0

    for i in range(len(a)):
        tg = a[i]
        ans += s.index(tg)
        s = [i for i in s if i != tg]

    print(ans)


if __name__ == "__main__":
    main()