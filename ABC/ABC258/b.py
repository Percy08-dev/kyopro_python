
def main():
    n = int(input())
    board = [list(map(int, list(input()))) for i in range(n)]

    M = max([max(i) for i in board])
    que = list()

    for i in range(n):
        for j in range(n):
            if board[j][i] == M:
                que.append((i, j, M))

    move = (
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,1),
        (1,1),
        (1,0),
        (1,-1),
        (0,-1)
    )

    ans = 0
    for i in range(len(que)):
        for dx, dy in move:
            point_mem = [que[i]]
            now_max = 0
            
            for _ in range(n-1):
                next_points = []
                now_max = point_mem[0][2]*10
                while len(point_mem) > 0:
                    x, y, num = point_mem.pop()
                    next_x = (x + dx) % n
                    next_y = (y + dy) % n 
                    if now_max < num*10 + board[next_y][next_x]:
                        now_max = num*10 + board[next_y][next_x]
                        next_points = [(next_x, next_y, now_max)]
                    elif now_max == num + board[next_y][next_x]:
                        next_points.append((next_x, next_y, now_max))
                point_mem = next_points

                ans = max(ans, now_max)

    print(ans)
    





if __name__ == "__main__":
    main()