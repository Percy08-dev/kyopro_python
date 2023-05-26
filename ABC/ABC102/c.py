import statistics
n = int(input())
a = list(map(int, input().split()))
b = [a[i] - i for i in range(n)]

median = int(statistics.median(b))

sad = 0
for i in range(n):
    sad += abs(median - b[i])
    
print(sad)