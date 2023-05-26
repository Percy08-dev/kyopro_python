

mod =  998244353 

def main():
    n = int(input())
    
    x = set([i for i in range(1, 10)])
    ans = len(x)

    for i in range(n-1):
        tmp = set()
        while len(x) > 0:
            mem = x.pop()
            if mem % 10 == 1:
                tmp.add(mem*10 + mem%10)
                tmp.add(mem*10 + mem%10 + 1)
            elif mem % 10 == 9:
                tmp.add(mem*10 + mem%10 - 1)
                tmp.add(mem*10 + mem%10)
            else:
                tmp.add(mem*10 + mem%10 - 1)
                tmp.add(mem*10 + mem%10)
                tmp.add(mem*10 + mem%10 + 1)

        x = tmp
        ans += len(x)
        print(len(x))
    





if __name__ == "__main__":
    main()