import itertools

def f(x):
    res = 0
    for i in range(len(x)):
        res += (i+1) * x[i]
    
    return res

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = f(a[:m])
    delta = sum(a[:m])
    tmp = ans

    for i in range(n-m):
        # print("{} - {} + {} = {}".format(ans, delta, a[i+m]*m, ans - delta + a[i+m]*m))
        tmp = tmp - delta + a[i+m] * m
        ans = max(ans, tmp)
        delta = delta - a[i] + a[i+m]
        



    print(ans)




if __name__ == "__main__":
    main()