import sys
n = int(input())
a = list(map(int, input().split()))
new = []

if n == 1:
    print(a[0])
    sys.exit()

ans = float("inf")

for i in range(2**(n-1)):
    mem0 = 0
    mem1 = 0
    for j in range(n):
        if (i >> j) & 1:
            mem0 = mem0 | a[j]
            mem1 = mem0 ^ mem1
            mem0 = 0
        else:
            mem0 = mem0 | a[j]

    if ans > mem1:
        ans = mem1

print(ans)
