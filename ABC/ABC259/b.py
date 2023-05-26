import math

def main():
    a, b, d = map(int, input().split())
    rad = math.radians(d)

    x = math.cos(rad) * a - math.sin(rad) * b
    y = math.sin(rad) * a + math.cos(rad) * b

    print(x, y)


if __name__ == "__main__":
    main()