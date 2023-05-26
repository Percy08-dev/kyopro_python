def main():
    n = int(input())
    p = [tuple(map(int, input().split())) for _i in range(n)]
    p = [(x+1000+1, y+1000+1) for (x, y) in p]
    grid = [[0 for i in range(2000+1+2)] for j in range(2000+1+2)]
    move = (    # (x, y)
        (0, 1), 
        (1, 1), 
        (1, 0), 
        (0, -1), 
        (-1, -1), 
        (-1, 0)
    )

    for (x, y) in p:
        grid[y][x] = 1
    
    checked = set()
    stuck = list()
    ans = 0

    for (x, y) in p:
        tmp = (x, y)
        if tmp in checked:
            continue
        checked.add(tmp)
        stuck.append(tmp)

        while stuck:
            now = stuck.pop()
            checked.add(now)

            for (dx, dy) in move:
                next_point = (now[0] + dx, now[1] + dy)
                if grid[next_point[1]][next_point[0]] == 1 and not(next_point in checked):
                    stuck.append(next_point)
        
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()