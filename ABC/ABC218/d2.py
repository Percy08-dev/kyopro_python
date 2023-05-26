n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

cnt  = 0
for i in range(n):
    for j in range(i + 1 ,n):
