import collections
n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = a + b
y = list(set(x))

for i in y:
    if x.count(i) == 1:
        print(i, end=" ")

