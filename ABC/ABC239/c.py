def points(p):
    res  =[]
    move = [
        (1, 2), 
        (2, 1), 
        (2, -1), 
        (1, -2), 
        (-1, -2), 
        (-2, -1), 
        (-2, 1), 
        (-1, 2)
    ]

    for i in move:
        res.append((p[0] + i[0], p[1] + i[1]))

    return res

def main():
    x1, y1, x2, y2 = map(int, input().split())
    p1 = (x1, y1)
    p2 = (x2, y2)

    tmp0 = points(p1)
    tmp1 = points(p2)

    if len(set(tmp0) & set(tmp1)) != 0:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()