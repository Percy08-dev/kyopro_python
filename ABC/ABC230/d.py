def main():
    n, d = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(n)]
    data.sort(key=lambda x:x[1])

    cnt = 0
    row = 1

    lp = data[0][1]
    rp = data[0][1] + (d-1)

    while row < n:
        while row < n and (lp <= data[row][0] <= rp or lp <= data[row][1] <= rp or (data[row][0] < lp and data[row][1] > rp)):
            row += 1
        if row < n:
            lp = data[row][1]
            rp = data[row][1] + (d-1)
        cnt += 1
        
    
    print(cnt)



if __name__ == "__main__":
    main()