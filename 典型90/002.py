def judge(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        
        if cnt < 0:
            return 0
    if cnt == 0:
        return 1
    else:
        return 0

def exc(num):
    s = ""
    for i in range(n):
        if (num >> i) & 1:
            s += ")"
        else:
            s += "("
    return s

# 0=( , 1=)
n = int(input())
res = []

if n%2 == 1:
    print()
else:
    start = 1 << (n-1)
    for i in range(start, 2**n, 2):
        s = exc(i)

        if judge(s):
            res.append(s)
        #print(i, s, judge(s))

res = sorted(res, key=str.lower)
for i in res:
    print(i)