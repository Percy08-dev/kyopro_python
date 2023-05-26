def up(data, x, y):
    cnt = 0
    for i in reversed(range(y)):
        if data[i][x] != "#":
            #print(x+1, i+1)
            cnt += 1
        else:
            break
    return cnt

def down(data, x, y):
    cnt = 0
    global h
    for i in range(y, h):
        if data[i][x] != "#":
            #print(x+1, i+1)
            cnt += 1
        else:
            break
    return cnt

def left(data, x, y):
    cnt = 0
    for i in reversed(range(x)):
        if data[y][i] != "#":
            #print(i+1, y+1)
            cnt += 1
        else:
            break
    return cnt

def right(data, x, y):
    cnt = 0
    global w
    for i in range(x+1, w):
        if data[y][i] != "#":
            #print(i+1, y+1)
            cnt += 1
        else:
            break
    return cnt

h, w, x, y = map(int, input().split())
x -= 1
y -= 1
x,y = y,x

s = []
for i in range(h):
    s.append(list(input()))

ans = up(s, x, y) + down(s, x, y) + left(s, x, y) + right(s, x, y)
print(ans)