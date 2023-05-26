import sys
from collections import deque

def main():
    n, x = map(int, input().split())
    jump = [tuple(map(int, input().split())) for i in range(n)]
    p = set()
    p.add(0)

    for a, b in jump:
        tmp = list(p)
        p.clear()
        for i in tmp:
            if i + a <= x:
                p.add(i + a)
            if i + b <= x:
                p.add(i + b)

    if x in p:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()