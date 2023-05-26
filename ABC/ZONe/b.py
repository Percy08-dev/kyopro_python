n, d, h = map(int, input().split())
ans = h/d

for i in range(n):
    dn, hn = map(int, input().split())
    a = (h - hn)/(d - dn)
    if ans > a:
        ans = a

print(h - ans*d)
