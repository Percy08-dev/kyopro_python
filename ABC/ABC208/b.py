import sys
p = int(input())
coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
cnt = 0
num = 0

for i in reversed(range(10)):
    for j in range(100):
        if num + coin[i] > p:
            break
        num += coin[i]
        cnt += 1
        if num == p:
            print(cnt)
            sys.exit()