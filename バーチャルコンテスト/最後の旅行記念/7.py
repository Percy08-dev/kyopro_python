def main():
    n, m, k = map(int, input().split())
    res = "No"
    
    for i in range(n+1):
        for j in range(m+1):
            if i*(m-j) + j*(n-i) == k:
                res = "Yes"
                break
        else:
            continue
        break
    



    print(res)



if __name__ == "__main__":
    main()