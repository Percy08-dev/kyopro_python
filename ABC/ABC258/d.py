def main():
    n, x = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(n)]

    time = 0
    shotest_stage = float("inf")
    skip_cost = 0

    for i in range(x):
        if i >= len(data):
            time += shotest_stage * (x - i)
            break
        else:
            if shotest_stage  <= data[i][0] + data[i][1] + skip_cost:
                time += shotest_stage + skip_cost
                skip_cost = 0
                shotest_stage = min(data[i][1], shotest_stage)
            else:
                time += shotest_stage
                skip_cost += data[i][0] + data[i][1]
                shotest_stage = min(data[i][1], shotest_stage)

    print(time)




if __name__ == "__main__":
    main()