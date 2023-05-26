def main():
    n = int(input())
    h = list(map(int, input().split()))
    dp = [0 for i in range(n)]
    
    dp[1] = abs(h[0] - h[1])
    for i in range(2, n):
        x = abs(h[i] - h[i-1])
        y = abs(h[i] - h[i-2])
        dp[i] = min(dp[i-1] + x, dp[i-2] + y)

    print(dp[-1])







if __name__ == "__main__":
    main()