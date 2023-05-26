def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    cnt = 0

    i = k - 1

    while i < n:
        cnt += a[i]
        i += k
        
    if i==0:
        cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()