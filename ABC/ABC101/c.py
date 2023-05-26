import math
n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
last = 0
# 条件が甘いから愚直な実装でも許される？
while 1:
    if res == 0:
        last += k
    else:
        last += k-1
    res += 1

    if last >= n:
        break

print(res)