from collections import deque
s = input()

m = deque()
rev = False

for i in s:
    if i == "R":
        rev = not rev
    elif rev:
        # m andにする理由は, 空文字列を除くため？
        if m and m[0] == i:
            m.popleft()
        else:
            m.appendleft(i)
    else:
        if m and m[-1] == i:
            m.pop()
        else:
            m.append(i)

if rev:
    m = reversed(m)
print("".join(m))