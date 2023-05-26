import bisect

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    q = [tuple(map(int, input().split())) for _ in range(x)]

    counter = dict()

    for i, v in enumerate(a):
        if v in counter:
            counter[v].append(i+1)
        else:
            counter[v] = [i+1]

    for (L, R, x) in q:
        if x in counter:
            tmp = counter[x]
            print(bisect.bisect_right(tmp, R) - bisect.bisect_left(tmp, L))
        else:
            print(0)



if __name__ == "__main__":
    main()