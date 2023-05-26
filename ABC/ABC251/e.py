import math

from numpy import append

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 == 0:
        s1 = 0
        s2 = 0
        for i in range(0, n-1, 2):
            s1 += a[i]
            s2 += a[i+1]
        print(min(s1, s2))
    else:
        num = [0, a[0]]
        res = 0
        for i in range(1, n):
            if i % 2 == 0:
                num.append(num[-2] + a[i])
            else:
                num.append(num[-2] + a[i])

        for i in range(n):
            



if __name__ == "__main__":
    main()