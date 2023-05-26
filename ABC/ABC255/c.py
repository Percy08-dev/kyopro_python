
INF = float("inf")

def f(start, d, i):
    return start + d*i


def main():
    x, a, d, n = map(int, input().split())

    if d < 0:
        start = a + d*(n-1) - x
        end = a - x
        d = -d
    else:
        start = a - x
        end = a + d*(n-1) - x

    if 0 <= start:
        res = start
    elif end < 0:
        res = -end
    else:
        res = INF
        left = 0
        right = n - 1

        while right - left > 1:
            t1 = abs(f(start, d, left))
            t2 = abs(f(start, d, right))
            
            if t1 < t2:
                res = min(res, t1)
                right = (left + right) // 2
            else:
                res = min(res, t2)
                left = (left + right) // 2
            
        
        res = min(res, abs(f(start, d, left)), abs(f(start, d, right)))

    print(res)


if __name__ == "__main__":
    main()