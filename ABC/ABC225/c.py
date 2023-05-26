


def main():
    n, m = map(int, input().split())

    B = [list(map(int, input().split())) for _ in range(n)]

    ans = "Yes"

    # 横チェックとB_{i, j}の条件にあっているかどうか
    for x in range(1, m):
        if B[0][x] - B[0][x-1] != 1 or (B[0][x]-1)%7 < (B[0][x-1]-1)%7:
            ans = "No"
            break
    else:
        # 縦チェック
        for x in range(m):
            for y in range(1, n):
                if B[y][x] - B[y-1][x] != 7:
                    ans = "No"
                    break
            else:
                continue
            break


    print(ans)



if __name__ == "__main__":
    main()