def main():
    N, W = map(int, input().split())
    w, v = [], []
    for _ in range(N):
        ww, vv = map(int, input().split())
        w.append(ww)
        v.append(vv)

    dp = [[0 for i in range(N+1)] for j in range(W+1)]

    for weight in range(W+1):
        for item in range(N):
            if weight >= w[item]:
                dp[weight][item+1] = max(dp[weight - w[item]][item] + v[item], dp[weight][item])
            else:
                dp[weight][item+1] = dp[weight][item]
        
    # [print(i) for i in dp]
    print(dp[-1][-1])


if __name__ == "__main__":
    main()