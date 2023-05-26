def main():
    n = int(input())
    data = [list(map(int, input().split())) for i in range(n)]

    time = sum([i[0]/i[1] for i in data])
    time /= 2 

    pre = 0
    l = 0
    for i in range(n):
        if pre + data[i][0]/data[i][1] < time:
            pre += data[i][0]/data[i][1]
            l += data[i][0]
        else:
            l += data[i][1] * (time-pre) 
            break

    print(l)


if __name__ == "__main__":
    import decimal
    main()