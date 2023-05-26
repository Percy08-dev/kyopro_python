
def f_max(x, used):
    res = 0
    mem = x[res]
    for i in range(len(x)):
        if not(i in used):
            if mem < x[i]:
                res = i
                mem = x[i]

    return res

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[0 for i in range(m)] for j in range(m)]
    used = [set() for i in range(m)]

    for i in range(m):
        dp[0][i] = a[n-i-1] * m
    
    for i in range(1, m):
        tmp = [a[x]*(m-i) for x in range(n)]
        # print(tmp)
        for j in range(m):
            mem = f_max(tmp[:n-j-1], used[j])
            dp[i][j] = dp[i-1][j] + tmp[mem]
            used[j].add(mem)

    print(max(dp[-1]))



if __name__ == "__main__":
    main()