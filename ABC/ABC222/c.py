def judge(p1, p2):
    if p1 == p2:
        return 0, 0
    G, C, P = "G", "C", "P"
    if p1 == G:
        if p2 == C:
            return 1, 0
        else:
            return 0, 1
    elif p1 == C:
        if p2 == G:
            return 0, 1
        else:
            return 1, 0
    else:
        if p2 == G:
            return 1, 0
        else:
            return 0, 1

    

def main():
    n, m = map(int, input().split())
    data = [[0, input(), i+1] for i in range(2*n)]
    

    for i in range(m):
        for k in range(n):
            p1 = 2*k
            p2 = 2*k+1
            rp1, rp2 = judge(data[p1][1][i], data[p2][1][i])
            data[p1][0] += rp1
            data[p2][0] += rp2

        data.sort(key=lambda x:x[2])
        data.sort(key = lambda x:x[0], reverse=True)

    for i in data:
        print(i[2])


if __name__ == "__main__":
    main()