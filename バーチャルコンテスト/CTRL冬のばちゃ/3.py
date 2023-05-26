def main():
    n, k = map(int, input().split())
    walk = [int(input()) for i in range(n)]

    s = 0
    for i in range(n):
        s += walk[i]
        if s >= k:
            res = i+1
            break

    print(res)

if __name__ == "__main__":
    main()