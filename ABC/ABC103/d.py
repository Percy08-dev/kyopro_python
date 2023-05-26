import operator
n, m= map(int, input().split())

x = [[0, 0] for i in range(m)]

for i in range(m):
    x[i][0], x[i][1] = map(int, input().split())

x = sorted(x, key = operator.itemgetter(1))

cnt = 0
end = 0

for i in range(m):
    if x[i][0] >= end:
        end = x[i][1]
        cnt += 1

print(cnt)

