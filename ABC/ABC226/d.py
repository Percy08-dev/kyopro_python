import math
def main():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    magic = set()

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            xd = data[j][0] - data[i][0]
            yd = data[j][1] - data[i][1]
            g = math.gcd(xd, yd)
            magic.add(tuple([xd//g, yd//g]))

    
    print(len(magic))

if __name__ == "__main__":
    main()