import math

M = 10**9 + 7

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()

    res = 1

    for i, j in enumerate(c):
        x = 0 if j - i < 0 else j - i
        res = (res * x) % M
    
    print(res)






if __name__ == "__main__":
    main()