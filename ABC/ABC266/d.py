from collections import deque


class D:
    def __init__(self, t, x, a) -> None:
        self.t = t
        self.x = x
        self.a = a
    

def main():
    n = int(input())
    sunuke = [D(*map(int, input().split())) for i in range(n)]    # [[t1, x1, a1], [t2, x2, a2], ...]

    que = deque()
    for i in range(min(4, n)):
        if sunuke[i].x / sunuke[i].t <= 1:
            que.append([i, sunuke[i].x, sunuke[i].a])    # index, 座標, 大きさ

    if que:
        ans = max(que, key=lambda x:x[2])[2]
    else:
        ans = 0

    while que:
        # print(que)
        now = que.popleft()
        di = 1

        if now[0] + di >= n:
            ans = max(ans, now[2])
            continue
        
        while now[0] + di < n and di < 5 :
            if abs(sunuke[now[0] + di].x - now[1]) / ((sunuke[now[0] + di].t - sunuke[now[0]].t)) <= 1:
                tmp = [now[0] + di, sunuke[now[0] + di].x, now[2] + sunuke[now[0] + di].a]
                que.append(tmp)
            di += 1

    print(ans)

if __name__ == "__main__":
    main()