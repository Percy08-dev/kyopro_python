from collections import deque

def solver(need):
    global nums
    global searched

    q = deque(need)

    while len(q) > 0:
        tmp = q.popleft() - 1
        if tmp in searched:
            continue
        else:
            searched.add(tmp)
            q.extend(nums[tmp])






def main():
    n = int(input())
    global nums
    global searched

    data = [list(map(int, input().split())) for _ in range(n)]
    nums = [i[2:] for i in data]

    need = data[-1][2:]
    searched = set()
    searched.add(len(data)-1)

    solver(need)
    # print(searched)

    print(sum([data[i][0] for i in searched]))



if __name__ == "__main__":
    main()