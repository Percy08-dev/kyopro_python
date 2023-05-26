n, m = map(int, input().split())

data = [[0, 0, 0] for i in range(n)]
for i in range(n):
    data[i] = list(map(int, input().split()))


res = 0

# x, y, zにそれぞれ1, -1のどちらを乗じて和をとったほうが大きいか
for bit in range(2**3):
    data_sum = []
    # ケーキはn個ある
    for i in range(n):
        tmp = 0
        # ケーキの評価要素は3つ
        for j in range(3):
            # bitと一つでも同じ位置に1が立っているとTrueになる -> 0b001, 0b010, 0b100を順に確認することで、それぞれの符号を決定
            if bit & (1 << j):
                tmp += data[i][j]
            else:
                tmp -= data[i][j]
        data_sum.append(tmp)

    # 最大値の選択
    # reverseしないと、m = 0の時に-0~endになってしまい間違い, 同時にsum(data_sum[-m:]) -> sum(data_sum[:m])に変更
    data_sum.sort(reverse=True)
    s = sum(data_sum[:m])
    res = max(res, s)

print(res)

