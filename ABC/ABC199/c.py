
from itertools import product


def main():
    n = int(input())
    s = list(input())
    q = int(input())

    cnt = 0

    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if cnt % 2 == 0:
                s[a-1], s[b-1] = s[b-1], s[a-1]
            else:
                if a >= n:
                    a -= n
                else:
                    a += n
                
                if b >= n:
                    b -= n
                else:
                    b += n
                
                s[a-1], s[b-1] = s[b-1], s[a-1]

        else:
            cnt += 1
        

    if cnt % 2 == 1:
        s_front = s[:n]
        s_back = s[n:]
        s = s_back + s_front

    print("".join(s))

if __name__ == "__main__":
    main()