# 多分, 遅延セグ木？
def main():
    q = int(input())
    t = []
    x = []
    mod = 2**20
    nums = [-1 for i in range(mod)]

    for _ in range(q):
        t1, t2 = map(int, input().split())
        t.append(t1)
        x.append(t2)

    for i in range(q):
        if t[i] == 1:
            nu


if __name__ == "__main__":
    main()