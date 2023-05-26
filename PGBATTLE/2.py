# ゼロの無い整数
x = list(input())

if "0" in x:
    first = x.index("0")
    x = [x[i] if i < first else "1" for i in range(len(x))]
    res = int("".join(x))
else:
    res = int("".join(x))

print(res)
