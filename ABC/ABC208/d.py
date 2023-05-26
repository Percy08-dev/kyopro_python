import heapq

def dfs(s, t, k):
    for i in range(k):
        for j in range(k):
            a = 0

n, m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(m)]

map = [[float("inf") for i in range(n)] for j in range(n)]

for i in range(m):
    map[road[i][0]-1][road[i][1]-1] = road[i][2]
    # x軸方向:行先 y軸方向:出発点

"""
for i in map:
    print(i)
"""

