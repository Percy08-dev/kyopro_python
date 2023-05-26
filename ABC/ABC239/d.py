
def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range (0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False

    return primes

def main():
    a, b, c, d = map(int, input().split())
    primes = set(list_primes(200))
    ans = True

    # 高橋君が選んだ数全てを青木君が素数に変えられる場合に青木君の勝ち
    for i in range(a, b + 1):
        tmp = False
        for j in range(c, d + 1):
            tmp |=  (i + j) in primes
        ans &= tmp

    if ans:
        print("Aoki")
    else:
        print("Takahashi")




if __name__ == "__main__":
    main()