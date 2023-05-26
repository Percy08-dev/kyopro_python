n, k = map(int, input().split())
print(sum([i*100 for i in range(1, n+1)])*k +  sum([i for i in range(1, k+1)]) * n)