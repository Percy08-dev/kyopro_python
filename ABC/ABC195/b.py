import math
import sys
a, b, w = map(int, input().split())

w *= 1000

maxi = w//a
mini = math.ceil(w/b)

if mini > maxi:
    print("UNSATISFIABLE")
else:
    print(mini, maxi)
