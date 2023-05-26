import math
a = list(map(int, input().split()))

num1 = 0
if (a[0] + a[2])/2 == a[1]:
    num1 = 0
elif (a[0] + a[2])/2 < a[1]:
    num1 += (a[1] - (a[0] + a[2])/2) * 2
else:
    num1 += (a[0] + a[2])/2 - a[1]

# num1 = int(num1)

"""
num2 = 0
if abs(a[0] - a[1]) > abs(a[1] - a[2]):
    num2 = abs(a[0] - a[1]) -  abs(a[1] - a[2])
else:
    num2 = abs(a[1] - a[2]) -  abs(a[0] - a[1])
"""

if int(num1) != math.ceil(num1):
    num1 += 2

# print(min(num1, num2))
print(int(num1))