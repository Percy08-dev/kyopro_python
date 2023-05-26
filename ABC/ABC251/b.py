from itertools import count


def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = set([i for i in a if i <= w])

    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] <= w:
                cnt.add(a[i] + a[j])
            else:
                continue
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] <= w:
                    cnt.add(a[i] + a[j] + a[k])

    print(len(cnt))


if __name__ == "__main__":
    main()