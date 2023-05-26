import math

def main():
    n, k = map(int, input().split())
    p = [tuple(map(int, input().split())) for _ in range(n)]

    counter = dict()
    b = False
    for i in p:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
        
        if counter[i] >= k:
            b = True


    if b:
        print("Infinity")
    else:
        used = set()
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if p[i] == p[j]:
                    continue
                x_d = p[i][0] - p[j][0]
                y_d = p[i][1] - p[j][1]
                d = math.gcd(x_d, y_d)
                x_d //= d
                y_d //= d

                # if (p[i][1]*x_d - p[i][0]*y_d, (y_d + 0.1)/(x_d+0.1)) in used:
                if (p[i][1]*x_d - p[i][0]*y_d, x_d, y_d) in used:
                    continue
                # used.add((p[i][1]*x_d - p[i][0]*y_d, (y_d + 0.1)/(x_d+0.1)))
                used.add((p[i][1]*x_d - p[i][0]*y_d, x_d, y_d))
                print("(x, y) = ({}, {})\ndx={}, dy={}".format(p[0], p[1], x_d, y_d))

                cnt = 0
                for m in range(n):
                    if m == i or  m == j:
                        continue

                    if x_d == 0:
                        if (p[m][1] - p[i][1]) % y_d == 0:
                            cnt += 1
                    elif y_d == 0:
                        if (p[m][0] - p[i][0]) % x_d == 0:
                            cnt += 1
                    else:
                        if (p[m][0] - p[i][0]) % x_d == 0 and (p[m][1] - p[i][1]) % y_d == 0:
                            cnt += 1

                if cnt >= k:
                    res += 1

        print(res)
        print(used)


if __name__ == "__main__":
    main()