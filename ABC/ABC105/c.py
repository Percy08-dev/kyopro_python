def ary(n):
    num = ""
    while n != 0:
        if n % 2 == 0:
            num = "0" + num
        else:
            num = "1" + num
            n -= 1
        n //= -2

    return num


n = int(input())

print(0 if n == 0 else ary(n))