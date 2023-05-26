import sys
import itertools
import copy

def c(m, n):
    x = 1
    for i in range(m-n+1, m+1):
        x *= i
    for i in range(1, n+1):
        x //= i

    return x

def p(n):
    x = 1
    for i in range(5 - n, 5):
        x *= i
    return x

def f(n):
    x = 24
    if n == 3:
        x //= 2
        x *= 3
        return x
    elif x == 1:
        return 16
    else:
        return 14


s = input()

maru = []
hatena = []
batu = []

for i in range(10):
    if s[i] == "o":
        maru.append(i)
    elif s[i] == "x":
        batu.append(i)
    else:
        hatena.append(i)

if len(maru) > 4 :
    print(0)
elif len(maru) == 4 :
    print(1)
elif len(maru) + len(hatena) < 4:
    ans = p(4)*(len(maru) + len(hatena)) - p(4)*len(maru)//(5 - len(maru))
    
else:
    print(24 * (len(maru) + len(hatena)) - 24 * len(maru) // (4 - len(maru) + 1))
