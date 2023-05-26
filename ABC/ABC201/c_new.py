import itertools
import copy
import math

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

ans = 0
m = []

if len(maru) > 4:
    print(0)
else:
    y = maru + (hatena + maru) * (4 - len(maru))
    for i in itertools.combinations(y, 4):
        if (m in sorted(i)):
            continue

        for j in list(set(i)):
            if i.count(j):
                m.append(sorted(i))
                break
        if not(m in sorted(i)):
            ans += 1

    print(m)
    print(ans)
