def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    stuck = [(None, 0)]  # (ball num, chain)
    now = a[0]
    cnt = 1
    chain = 1
    print(1)

    for i in a[1:]:
        cnt += 1
        if now == i:
            chain += 1
        else:
            stuck.append((now, chain))
            now = i
            chain = 1
        
        if now == chain:
            cnt -= chain
            now, chain = stuck.pop()

        print(cnt)


if __name__ == "__main__":
    main()