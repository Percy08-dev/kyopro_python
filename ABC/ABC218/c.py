def turn(data):
    global n
    res = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[n- j - 1][i]  = data[i][j]

    return res

def out(data):
    global n
    for i in range(n):
        print(data[i])

def equal(data1, data2):
    # 縦
    for i in range(n):
        data1 = data1[1:] + [data1[0]]
        if data1 == data2:
            return "Yes"
        
    



n = int(input())

s = []
for _ in range(n):
    s.append(list(input()))

t = []
for _ in range(n):
    t.append(list(input()))

equal(s, t)