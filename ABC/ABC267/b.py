def main():
    s = input()
    x = [
        [int(s[6])], 
        [int(s[3])], 
        [int(s[1]), int(s[7])], 
        [int(s[0]), int(s[4])], 
        [int(s[2]), int(s[8])], 
        [int(s[5])], 
        [int(s[9])]
    ]

    y1 = s[0] == "0"
    y2 = [sum(i) for i in x]
    

    ans = "No"

    if y1:
        for i in range(6):
            for j in range(i+1, 7):
                for k in range(i+1, j):
                    if sum(x[i]) and sum(x[j]) and sum(x[k]) == 0:
                        ans = "Yes"

    print(ans)


if __name__ == "__main__":
    main()