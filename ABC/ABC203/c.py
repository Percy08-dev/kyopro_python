import sys
n, k = map(int, input().split())
cnt = 0

f = [list(map(int, input().split())) for _ in range(n)]
f.sort()

if k - f[0][0] >= 0:
    k += f[0][1] - f[0][0]
    cnt = f[0][0]
else:
    print(k)
    sys.exit()

for i in range(1, n):
    if k - (f[i][0] - f[i-1][0]) >= 0:
        k += f[i][1] - (f[i][0] - f[i-1][0])
        cnt = f[i][0]
    else:
        break
    

cnt += k


print(cnt)