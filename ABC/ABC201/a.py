a = list(map(int, input().split()))
ans = "No"

a.sort()

if a[2] - a[1] == a[1] - a[0]:
    print("Yes")
else:
    print("No")

    