import math

def main():
    n, k = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(range(1, n+1)).difference(a)

    p = [tuple(map(int, input().split())) for i in range(n)]

    dist = set()

    for i in b:
        tmp = float("inf")
        for j in a:
            d = (p[i-1][0] - p[j-1][0]) * (p[i-1][0] - p[j-1][0]) + (p[i-1][1] - p[j-1][1]) * (p[i-1][1] - p[j-1][1])
            tmp = min(tmp, d)
        dist.add(tmp)

    print(math.sqrt(max(dist)))






if __name__ == "__main__":
    main()