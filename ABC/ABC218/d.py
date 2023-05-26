import math 
def main():
    n = int(input())

    xd = dict()
    yd = dict()

    for _ in range(n):
        x, y = map(int, input().split())
        if x in xd:
            xd[x].append(y)
        else:
            xd[x] = [y]

    cnt = 0
    xdi = list(xd.items())
    for i in range(len(xdi)):
        for j in range(i+1, len(xdi)):
            product = set(xdi[i][1]) & set(xdi[j][1])
            cnt += math.comb(len(product), 2) 

    print(cnt)



if __name__ == "__main__":
    main()