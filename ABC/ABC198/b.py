n = input()

if len(n) == 1:
    print("Yes")
elif n[-1] == "0":
    for i in reversed(range(len(n) - 1)):
        if n[i] != "0":
            c = i
            break
    n = n[:i + 1]
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")
else:
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")