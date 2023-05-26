# lb以上の長さで分割した場合の領域の数
def split_cnt(lb):
    l = 0
    cnt = 0
    for i in a:
        l += i
        if l >= lb:
            l = 0
            cnt += 1

    return cnt


# 
def biserch(right, left):
    while (right - left) > 1:
        mid  = (left + right)//2
        if split_cnt(mid) >= k+1:
            left = mid
        else:
            right = mid
    return left


n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
a = [0] + a
a.append(l)

a = [a[i+1] - a[i] for i in range(n+1)]


print(biserch(l+1, -1))