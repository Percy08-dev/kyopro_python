# 一点封鎖
import math

n, m, a, b = map(int, input().split())

if n < a or m < b:
    res = math.factorial(n + m)//(math.factorial(n) * math.factorial(m))
    res %= 998244353
else:
    ALL = math.factorial(n + m)//(math.factorial(n) * math.factorial(m))
    BUT = (math.factorial(a + b)//(math.factorial(a) * math.factorial(b)) ) * (math.factorial(n - a + m - b) // (math.factorial(n - a) * math.factorial(m - b)))
    res = (ALL - BUT) % 998244353

print(res)