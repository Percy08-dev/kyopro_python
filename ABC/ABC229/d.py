def rle(s:str):
    res = []
    tmp = [s[0], 1]
    for i in range(1, len(s)):
        if s[i] != tmp[0]:
            res.append(tmp)
            tmp = [s[i], 1]
        else:
            tmp[1] += 1
    res.append(tmp)

    return res


# k == 0
def solver1(s):
    s = rle(s)
    s = [i for i in s if i[0] == "X"]
    if len(s) == 0:
        res = ["X", 0]
    else:
        res = max(s, key=lambda x:x[1])
    return res[1]


def solver2(s, k):
    ans = 0
    r = 1

    if s[0] == ".":
        S = 1
        tmp = 1
    else:
        S = 0
        tmp = 1
    
    for left in range(len(s)-1):
        while r < len(s):
            if s[r] == "." and S + 1 <= k:
                S += 1
                tmp += 1
            elif s[r] == "X":
                tmp += 1
            else:
                break

            r += 1
        ans = max(ans, tmp)

        if s[left] == ".":
            tmp -= 1
            S -= 1
        else:
            tmp -= 1

    return max(ans, tmp)


def main():
    s = input()
    k = int(input())

    if k == 0:
        ans = solver1(s)
    else:
        ans = solver2(s, k)


    print(ans)






if __name__ == "__main__":
    main()