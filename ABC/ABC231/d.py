# from typing import Dict

class node:
    def __init__(self) -> None:
        self.left = None
        self.right = None


def add(R:dict, a, b):
    f = True
    if not(a in R):
        R[a] = node()
    if not(b in R):
        R[b] = node()
    
    if R[a].left == None and R[b].right == None:
        R[a].left = b
        R[b].right = a
    elif R[a].right == None and R[b].left == None:
        R[a].right = b
        R[b].left = a
    elif R[a].right == None and R[b].right == None:
        R[a].right = b
        R[b].right = a
    elif R[a].left == None and R[b].left == None:
        R[a].left = b
        R[b].left = a
    else:
        f = False
    
    return f



def circ(R:dict)->bool:
    data = set(R.keys())
    flag = True

    while data and flag:
        mem = data.pop()
        p = mem
        while R[p].right != None:
            if p == R[mem].left:
                flag = False
                break
            else:
                if p in data:
                    data.remove(p)
                p = R[p].right

    return flag




def main():
    n, m = map(int, input().split())
    # 経路の個数と円環の検出
    R = dict()
    f = True

    for i in range(m):
        a, b = map(int, input().split())
        f = add(R, a, b)
        if not(f):
            break
    else:
        f = circ(R)
    
    if f:
        print("Yes")
    else:
        print("No")






if __name__ == "__main__":
    main()