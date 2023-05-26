import math
a, b, c, d  = map(int, input().split())
cnt = 0

upper = b // c
lower = (a-1) // c

cnt += upper - lower

upper =  b // d
lower = (a-1) // d

cnt += upper - lower

upper =  b // ((c*d)//math.gcd(c, d))
lower = (a-1) // ((c*d)//math.gcd(c, d))

cnt -= upper - lower

print(b - a + 1 - cnt)