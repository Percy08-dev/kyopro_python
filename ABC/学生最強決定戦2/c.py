import sys

def gcd(x, y):
    if y == 0 :
        return x
    else:
        return gcd(y, x % y)

def era(n):
    if not isinstance(n, int):
        raise TypeError("n is int-type.")
    if n < 2:
        raise ValueError("n is more than 2")
    data = [i for i in range(2, n + 1)]
    for d in data:
        data = [x for x in data if (x == d or x % d != 0)]
    return data

a, b= map(int, input().split())

for i in reversed(range(1, b+1)):
    for j in range(2, b):
        if i*j > b:
            break
        if a <= i*(j-1) and b >= i*j:
            print(i)
            sys.exit()
print(1)
