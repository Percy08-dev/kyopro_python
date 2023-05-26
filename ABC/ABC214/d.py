from typing import SupportsAbs


n = int(input())

s = 0
wl = [[0 for i in range(n)] for j in range(n)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    wl[min(u, v)-1][max(u, v)-1] = w
    
for i in range(n):
    mem = 0
    for j in range(i, n):
        for k in range(i, j+1):
            mem = max(mem, max(wl[k]))
            print(wl[k])
        s += mem
    for j in reversed(range(i, n)):
        mem = max(mem, max(wl[j]))
        print(wl[j])
    s += mem

for i in range(n):
    print(wl[i])

print(s)
