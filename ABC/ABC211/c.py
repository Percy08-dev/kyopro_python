import itertools
import copy

def check(aru, wakaranai, t):
    f_list = set()
    cnt = 0
    for i in t:
        if i in aru:
            f_list.add(i)
            cnt += 1
        elif i in wakaranai:
            cnt += 1

    if cnt == 4 and f_list == set(aru) :
        return True
    else:
        return False
        


def main():
    s = input()
    cnt = 0

    aru = []
    nai = []
    wakaranai = []

    for i in range(len(s)):
        if s[i] == "o":
            aru.append(i)
        elif s[i] == "x":
            nai.append(i)
        else:
            wakaranai.append(i)

    nums = [i for i in range(10)]

    cnt = len([1 for i in itertools.product(nums, repeat=4) if check(aru, wakaranai, i)])


    print(cnt)
    return





if __name__ == "__main__":
    main()

