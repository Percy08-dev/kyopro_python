def main():
    a, b, c, x = map(int, input().split())

    if x <= a:
        ans = 1.0
    elif x <= b:
        ans = c/(b-a)
        if ans > 1:
            ans = 1.0
    else:
        ans = 0

    print(ans)

if __name__ == "__main__":
    main()