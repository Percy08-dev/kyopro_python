
def ans(x, y):
    print("! {} {}".format(x, y), flush=True)

def question(q):
    print("? {} {} {} {}".format(*q), flush=True)
    return int(input())


def x_serch(left, right, n):   # a <= i <= b
    mid = (left + right) // 2
    query = (left, mid, 1, n)
    num = question(query)

    if num < (mid - left + 1):
        return left, mid
    else:
        return mid + 1, right


def y_serch(bottom, top, n):    # c <= j <= d
    mid = (bottom + top) // 2
    query = (1, n, bottom, mid)
    num = question(query)

    if num < (mid - bottom + 1):
        return bottom, mid
    else:
        return mid + 1, top



def main():
    n = int(input())

    VH_Flag = True
    left = 1
    right = n
    bottom = 1
    top = n

    for _i in range(20):
        if VH_Flag:
            left, right = x_serch(left, right, n)
            if bottom != top:
                VH_Flag = not(VH_Flag)
        else:
            bottom, top = y_serch(bottom, top, n)
            if left != right:
                VH_Flag = not(VH_Flag)
        # print("turn:{}, left:{}, right:{}, top:{}, bottom:{}".format("x" if VH_Flag else "y", left, right, top, bottom))
        if left == right and top == bottom:
            break

    ans(left, top)



if __name__ == "__main__":
    main()