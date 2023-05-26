r, x, y = map(int, input().split())
n = x**2 + y**2
m = r**2
for i in range(1, 10**5 + 1):
    if n <= (i**2)*m:
        print(i)
        break