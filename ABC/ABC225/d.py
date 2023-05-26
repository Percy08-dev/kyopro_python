from typing import List


class bidirection:
    def __init__(self, prev, next) -> None:
        self.prev = prev
        self.next = next

def qp(train:List[bidirection], n):
    start = n
    if train[start].prev == -1:
        pass
    else:
        while train[start].prev != -1:
            start = train[start].prev

    ans = []
    while start != -1:
        ans.append(start)
        start = train[start].next

    print(len(ans), *ans)


def main():
    n, q = map(int, input().split())

    train = [bidirection(-1, -1) for _ in range(n+1)]

    for i in range(q):
        que = list(map(int, input().split()))

        if que[0] == 1:
            train[que[1]].next = que[2]
            train[que[2]].prev = que[1]
        elif que[0] == 2:
            train[que[1]].next = -1
            train[que[2]].prev = -1
        else:
            qp(train, que[1])



if __name__ == "__main__":
    main()