import itertools

a, b, k =  map(int, input().split())

lm = ["" for i in range(a+b)]

cnt = 1

for i in range(k):
    if (2**k-1 >> i) & 1:
        lm[i] ="b"
    else:
        lm[i] ="a"

print("".join(lm))
