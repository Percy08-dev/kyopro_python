n = int(input())
x = list(map(int, input().split()))

y = 1
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

divisor = [[] for i in range(n)]

for i in range(n):
    for j in prime:
        if x[i] % j == 0:
            divisor[i].append(j)

d = []
for i in divisor:
    if not(i[0] in d):
        d.append(i[0])

for i in d:
    y *= i

mem = divisor[0][0]
# n個の合成数
for i in range(n):
    # n番目の約数listを順に確認
    for j in range(len(divisor[i])):
        # i番目の約数listのj番目の数はk番目の約数listに含まれるかどうか
        for k in range(i+1):
            if not(divisor[i][j] in divisor[k]):
                if j == 0 and mem % divisor[i][j] != 0:
                    mem *= divisor[i][j]
                break
            elif k == i:
                if mem > divisor[i][j]:
                    mem = divisor[i][j]
        else:
            continue
        break
    


print(min(mem, y))
print((mem, y))

