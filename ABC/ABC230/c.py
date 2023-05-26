def draw(x, y, board, op, xstart, ystart):
    for k in range(x, y+1):
        board[ystart+k][xstart+k*op] = "#"

    return board

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())

    board = [["." for i in range(s-r+1)] for j in range(q-p+1)]

    ystart = a-p
    xstart = b-r

    board = draw(max(p-a, r-b), min(q-a, s-b), board, +1, xstart, ystart)
    board = draw(max(p-a, b-s), min(q-a, b-r), board, -1, xstart, ystart)

    for i in board:
        print("".join(i))


if __name__ == "__main__":
    main()