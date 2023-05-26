import bisect
l, q = map(int, input().split())

woods = [l]

for i in range(q):
    c, x = map(int, input().split())
    if c == 1:
        n = bisect.bisect_left(woods, x)
        woods = n[]
    else:
        n = bisect.bisect_left(woods, x)
        print(n)

