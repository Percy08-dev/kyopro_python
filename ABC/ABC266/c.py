import math

class P:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class V:
    # p1 -> p2
    def __init__(self, p1:P, p2:P) -> None:
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y
    
    def ang(self, other):
        cos = (self.x*other.x + self.y*other.y) / (math.sqrt(self.x * self.x + self.y * self.y) * math.sqrt(other.x * other.x + other.y * other.y))
        ang = math.acos(cos)
        ang = math.degrees(ang)

        if self.pro(other):
            ang = 360 - ang

        return ang

    # z成分は0
    # True -> left, False -> right
    def pro(self, other):
        dig = self.x * other.y - self.y * other.x
        # print(dig)
        return dig >= 0



def main():
    a = P(*map(int, input().split()))
    b = P(*map(int, input().split()))
    c = P(*map(int, input().split()))
    d = P(*map(int, input().split()))

    # dab
    ad = V(a, d)
    ab = V(a, b)
    dab = ad.ang(ab)

    # abc
    ba = V(b, a)
    bc = V(b, c)
    abc = ba.ang(bc)

    # bcd
    cb = V(c, b)
    cd = V(c, d)
    bcd = cb.ang(cd)

    # cda
    dc = V(d, c)
    da = V(d, a)
    cda = dc.ang(da)

    # print(dab, abc, bcd, cda)

    if dab < 180 and abc < 180 and bcd < 180 and cda < 180:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()