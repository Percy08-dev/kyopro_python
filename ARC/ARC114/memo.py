data = dict(zip(prime, [0]*len(prime)))

for i in divisor:
    for j in i:
        data[j] += 1

value = data.values()
if n in value:
    print(get_key(value, n))
else:
    

候補
・それぞれの合成数の最小の因数の積
・もっとも多く共通して含まれる因数の積

for i in range(n):
    for j in range(i):
        if not(divisor[i][0] in divisor[j]):
            break
    else:
        mem = divisor[i][0]
        continue
    mem *= divisor[i][0]
