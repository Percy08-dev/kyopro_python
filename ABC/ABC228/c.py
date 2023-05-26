import bisect

def main():
    n, k = map(int, input().split())
    data = [sum(map(int, input().split())) for _ in range(n)]

    # narabi = [*range(n)]
    # before_sort_index = sorted(narabi, key=lambda i:data[i])
    rank = sorted(data)
    if_rank = [bisect.bisect_right(rank, i+300) + 1 for i in data]

    for i in if_rank:
        if n - i + 2 <= k:
            print("Yes")
        else:
            print("No")
    
    #print(if_rank)
    #print([n - i + 2 for i in if_rank])


if __name__ == "__main__":
    main()