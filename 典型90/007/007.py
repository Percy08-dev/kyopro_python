import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for i in range(q)]

a.sort()
#print(a)

#print("--------------------------------------------")

for i in range(q):
    ans = bisect.bisect_left(a, b[i]) 
    # ansの位置がaの最後尾の場合, 配列外参照が起こる.
    if len(a) > ans:
        diff1 = abs(b[i] - a[ans])
        diff2 = abs(b[i] - a[ans-1])
    else:
        diff1 = float("inf")
        diff2 = abs(b[i] - a[ans-1])
    print(min(diff1, diff2))