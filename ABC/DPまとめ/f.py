def LCS(s1, s2):
    L1 = len(s1) + 1
    L2 = len(s2) + 1
    dp = [[0 for i in range(L2)] for j in range(L1)]
    ans = ""
    for i in range(1, L1):
        for j in range(1, L2):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    ans = ""
    i, j = L1-1, L2-1
    while i >= 1 and j >= 1:
        if s1[i - 1] == s2[j - 1]:
            ans += s1[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                j -= 1

    return ans[::-1]



def main():
    s = input()
    t = input()

    ans = LCS(s, t)

    print(ans)



if __name__ == "__main__":
    main()