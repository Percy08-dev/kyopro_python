n = int(input())
ans = "No"
for i in range(26):
    for j in range(15):
        if i*4 + j*7 == n:
            ans = "Yes"
            break
    else:
        continue
    break

print(ans)
