# a全体のlcmを求めることで, 任意のmに対して sum(m mod a[i]) = sum(a[i] - 1)となる ( lcm -1)
n = int(input())
a = list(map(int, input().split()))

s = 0
for i in a:
    s += i - 1

print(s)