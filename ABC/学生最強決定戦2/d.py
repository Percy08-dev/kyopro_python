n, p = map(int, input().split())
mod = 10**9 + 7

x = pow(p-2, n-1, mod)
print(x)
print(x * (p-1) % mod)