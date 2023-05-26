def inc(n):
    return n + 1

n = int(input())
p = list(map(int, input().split()))

ans = [i for i in range(n)]

ans = sorted(ans, key = lambda x: p[x])
ans = list(map(inc, ans))

print(*ans)