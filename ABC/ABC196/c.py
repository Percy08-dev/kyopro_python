import math
import sys
n = input()
l = len(n) // 2

if l == 0:
    print(0)
    sys.exit()


n0 = int(n[:l])
n1 = int(n[l:])

if len(n) % 2 == 0:
    if n0 <=  n1:
        print(n0)
    else:
        print(int(n0) - 1)
else:
    print("9" * l)