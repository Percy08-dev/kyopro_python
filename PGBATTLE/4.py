# 無双関数
import itertools
n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))

res = 0
com = itertools.accumulate(s)

mem = []
# iまでの領域で重複しない部分を切り取る
tmp = set()
for i in range(n):
    if a[i] in tmp:
        mem.append(i)
        tmp = set()
    else:
        tmp.add(a[i])

if len(mem) == 0:
    res = com[-1]
else:


print(mem)


print(res % 998244353)