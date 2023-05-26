n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

cnt = 0
sb = 0
sc = 0


for i in range(n):
    if sb == n or sc == n:
        break
    for j in range(sb, n):
        if a[i] < b[j]:
            sb = j
            break
    
    for k in range(sc, n):
        if b[sb] < c[k]:
            sc = k
            break

    if a[i] < b[sb] and b[sb] < c[sc]:
        cnt += 1
    sb += 1
    sc += 1

print(cnt)