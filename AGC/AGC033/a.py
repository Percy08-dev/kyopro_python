from collections import deque

def bfs(q, distance):
    while q:
        h, w = q.popleft()
        d = distance[h][w]

        for dy, dx in ((1,0), (0,1), (-1,0), (0,-1)):
            new_h = h + dy
            new_w = w + dx
            # 範囲外の判定
            if new_h < 0 or len(distance) <= new_h or new_w < 0 or len(distance[0]) <= new_w:
                continue
            if distance[new_h][new_w] == -1:    # 更新されてないマスは-1
                distance[new_h][new_w] = d + 1  # 距離の加算
                q.append((new_h, new_w))
        
    return d



def main():
    h, w = map(int, input().split())
    board = [input() for _ in range(h)]
    # 元々の黒点からの距離を記録
    distance = [[-1 for i in range(w)] for j in range(h)]

    q = deque()

    for i in range(h):
        for j in range(w):
            if board[i][j] == "#":
                q.append((i, j))
                distance[i][j] = 0      # 黒の距離はゼロ

    ans = bfs(q, distance)
    print(ans)


if __name__ == "__main__":
    main()