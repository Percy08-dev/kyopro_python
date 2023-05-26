n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = [0 for i in range(n)]

mem = t[0]

for i in range(2*n):
    if t[i%n] <= mem + s[i%n-1]:
        ans[i%n] = t[i%n]
        mem = t[i%n]
    else:
        ans[i%n] = mem + s[i%n-1]
        mem += s[i%n-1]

for i in ans:
    print(i)