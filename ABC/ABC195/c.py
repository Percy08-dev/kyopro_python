n = int(input())

ans = 0
num = 999

while n >= num:
    ans += n - num
    num = num*10**3 + 999

print(ans)