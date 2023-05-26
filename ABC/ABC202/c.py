n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

x = [0 for i in range(n+1)]
y = [0 for i in range(n+1)]
z = [0 for i in range(n+1)]

for i in a:
    x[i] += 1

for i in b:
    y[i] += 1


cnt = 0

for i in c:
    cnt += x[b[i-1]] 

print(cnt)
