import operator
import sys

def clac_point(data):
    global g
    mem = [0, 0]
    for i in data:
        for j in range(i[0]):
            mem[0] += 100*i[2]
        else:
            mem[0] += 



d, g = map(int, input().split())
data = []

# 得点の大きいほうから解いていったほうがいいか、コンプリートボーナスをとるようにしたほうが良いか
# data -> q_count, bonus, i
for i in range(d):
    x = list(map(int, input().split()))
    x.append(i+1)
    data.append(x)

print(data)
comb = []

for i in range(2**d):
    bag = []
    for j in range(i):
        if (i >> j) & 1:
            bag.append(data[i])
    comb.append(bag)

res = [float("inf"), float("inf")]

for i in comb:
    mem = [0, 0]
    