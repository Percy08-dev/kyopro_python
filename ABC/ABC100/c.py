n = int(input())
a = list(map(int, input().split()))

cnt = -1
num = 0
while cnt != 0:
    cnt = sum(i%2==0 for i in a)
    
    num += cnt
    
    for i in range(n):
        if a[i]%2 == 0:
            a[i] //= 2


print(num)