n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

data.sort(key=lambda x:x[1])

time = 0
for i in data:
    time += i[0]
    if time > i[1]:
        ans = "No"
        break
else:
    ans = "Yes"

print(ans)
