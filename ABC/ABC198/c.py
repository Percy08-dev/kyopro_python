import math
from decimal import Decimal
r, x, y = map(int, input().split())

d = Decimal(x**2 + y**2)
n = Decimal(r**2)
if r**2 > d:
    print(2)
else:
    print(math.ceil((d/n).sqrt()))