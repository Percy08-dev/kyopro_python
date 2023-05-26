def main():
    n = int(input())
    happyness = [list(map(int, input().split())) for i in range(n)]

    dp = [[0 for i in range(n)] for j in range(3)]

    dp[0][0] = happyness[0][0]
    dp[1][0] = happyness[0][1]
    dp[2][0] = happyness[0][2]

    for i in range(1, n):
        for j in range(3):
            if j == 0:
                tmp = max(dp[1][i-1] + happyness[i][0], dp[2][i-1] + happyness[i][0])
            elif j == 1:
                tmp = max(dp[0][i-1] + happyness[i][1], dp[2][i-1] + happyness[i][1])
            else:
                tmp = max(dp[0][i-1] + happyness[i][2], dp[1][i-1] + happyness[i][2])
            dp[j][i] = tmp

    print(max(dp[0][-1], dp[1][-1], dp[2][-1]))



if __name__ == "__main__":
    main()