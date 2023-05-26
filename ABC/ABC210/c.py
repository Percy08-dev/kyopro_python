class colors(dict):
    def __init__(self):
        self.num = 0
        self.res = 0
    
    def inc(self, x):
        if x in self:
            if self[x] == 0:
                self.num += 1
                self.res = max(self.num, self.res)
            self[x] += 1
        else:
            self[x] = 1
            self.num += 1
            self.res = max(self.num, self.res)
        
    def dic(self, x):
        if x in self:
            self[x] -= 1
            if self[x] == 0:
                self.num -= 1
    


def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    tmp = colors()

    for i in range(k):
        tmp.inc(c[i])

    for i in range(k, n):
        tmp.dic(c[i-k])
        tmp.inc(c[i])
        # print(tmp.res, tmp)

    print(tmp.res)


if __name__ == "__main__":
    main()