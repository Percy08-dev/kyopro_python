

from operator import index
from sqlite3 import adapt


def main():
    n = int(input())
    name = set()
    data = []
    
    for i in range(n):
        s, t = input().split()
        if s in name:
            data.append(0)
        else:
            data.append(int(t))
            name.add(s)


    m = max(data)


    print(data.index(m) + 1)





if __name__ == "__main__":
    main()