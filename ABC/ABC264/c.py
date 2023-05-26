import sys

def popcount(x):
    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

def f(ax, ay):
    res = True
    bx = 0
    by = 0
    for shi1 in range(h1):
        if ay >> shi1 & 1 == 0:
            continue
        for shi2 in range(w1):
            if ax >> shi2 & 1 == 0:
                continue
            res = res and a[shi1][shi2] == b[by][bx]
            if not(res):
                return False
            bx += 1
        bx = 0
        by += 1

    return True


def main():
    global a, b, h1, w1

    h1, w1 = map(int,input().split())
    a = [list(map(int, input().split())) for i in range(h1)]

    h2, w2 = map(int,input().split())
    b = [list(map(int, input().split())) for i in range(h2)]


    for ay in range(2**h1):
        if popcount(ay) != h2:
            continue
        for ax in range(2**w1):
            if popcount(ax) != w2:
                continue
            if f(ax, ay):
                print("Yes")
                sys.exit()
            
    print("No")



if __name__ == "__main__":
    main()