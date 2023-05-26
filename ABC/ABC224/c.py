def check(p1, p2, p3):
    return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0] - p3[0])*(p1[1]-p3[1]) != 0


def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                cnt += check(points[i], points[j], points[k])

    print(cnt)




if __name__ == "__main__":
    main()