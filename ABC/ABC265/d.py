
def bis(left, right, vec, base, tg):
    res = (False, -1)
    while left <= right:
        mid = (left + right) //2
        
        if base + vec[mid] == tg:
            res = (True, mid)
            break
        elif base + vec[mid] < tg:
            left = mid + 1
        else:
            right = mid - 1

    return res


def main():
    N, P, Q, R = map(int, input().split())
    a = list(map(int, input().split()))
    sums = [0 for i in range(N+1)]
    for i in range(1, N+1):
        sums[i] = sums[i-1] + a[i-1]
    
    ans = "No"

    for x in range(N):
        y = bis(x, N, sums, -sums[x], P)
        if not(y[0]):
            continue
        z = bis(y[1] + 1, N, sums, -sums[y[1]], Q)
        if not(z[0]):
            continue
        w = bis(z[1] + 1, N, sums, -sums[z[1]], R)
        if w[0]:
            ans = "Yes"
            break
    
    print(ans)





if __name__ == "__main__":
    main()