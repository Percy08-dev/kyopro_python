def main():
    s, t, x = map(int, input().split())
    
    if s > t:
        if x < t or s <= x < t + 24:
            print("Yes")
        else:
            print("No")
    else:
        if s <= x < t:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()