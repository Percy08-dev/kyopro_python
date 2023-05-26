a = list(map(int, input().split()))
a.sort()
res = 0
for i in range(1, len(a)):
    res += a[i] - a[i-1]

print(res)