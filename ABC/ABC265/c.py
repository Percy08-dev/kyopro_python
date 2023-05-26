class P:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def fm(self) -> tuple:
        return (self.x, self.y)

def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]

    p = P(0, 0)
    ans = P(0, 0)
    ps = set()

    while 0 <= p.y < h and 0 <= p.x < w:
        ans = p
        if g[p.y][p.x] == "U":
            p = p + P(0, -1)
        elif g[p.y][p.x] == "D":
            p = p + P(0, 1)
        elif g[p.y][p.x] == "L":
            p = p + P(-1, 0)
        elif g[p.y][p.x] == "R":
            p = p + P(1, 0)
        
        tmp = p.fm()
        if tmp in ps:
            print(-1)
            break
        else:
            ps.add(tmp)
    else:
        print(ans.y + 1, ans.x + 1)




if __name__ == "__main__":
    main()