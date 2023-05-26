n, k = map(int, input().split())
a = list(map(int, input().split()))

max_num = k // n

r = list(range(n))
r1 = list(range(n))

r.sort(key = a.__getitem__)
r1.sort(key = r.__getitem__)

#print(r)
#print(a)

for i in range(n):
    print(max_num + 1 if r1[i] < k % n else max_num)