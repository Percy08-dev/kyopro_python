def RLE_sim(s):
    i = 1
    res = [s[0]]

    while i < len(s):
        x = res[-1]

        if x == s[i]:
            d = 0
            while i+d < len(s) and x == s[i+d]:
                d += 1

            if d > 0:
                res.append(x)
                if i+d < len(s):
                    res.append(s[i+d])
                i += d
        else:
            res.append(s[i])

        i += 1



    return "".join(res)


def RLE_sim2(s):
    i = 0
    res = []
    x = [s[0], 0]

    while i < len(s):
        d = 0
        while i+d < len(s) and s[i] == s[i+d]:
            d += 1
        x[1] = d
        res.append(x)

        if i+d < len(s):
            x = [s[i+d], 0]

        i += d
    
    return res



def main():
    s = input()
    t = input()

    s_p = RLE_sim2(s)
    t_p = RLE_sim2(t)

    # print(s_p)
    # print(t_p)

    f = len(s_p) == len(t_p)

    for i in range(min(len(s_p), len(t_p))):
        f = f & (s_p[i][0] == t_p[i][0] and (s_p[i][1] <= t_p[i][1] if s_p[i][1] > 1 else s_p[i][1] == t_p[i][1]) )



    # if RLE_sim(s) == RLE_sim(t) and len(s) <= len(t):
    if f:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()