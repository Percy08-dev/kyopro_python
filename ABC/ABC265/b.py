def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    for _i in range(m):
        x, y = map(int, input().split())
        a[x-1] -= y
    
    ans = "Yes"

    for i in a:
        t -= i
        if t <= 0:
            ans = "No"
            break
    if t <= 0:
            ans = "No"

    print(ans)



if __name__ == "__main__":
    main()