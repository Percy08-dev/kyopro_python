n, k = map(int, input().split())
digit = len(str(n))

map = [[float("inf") for i in range(n)] for j in range(n)]

for i in range(m):
    