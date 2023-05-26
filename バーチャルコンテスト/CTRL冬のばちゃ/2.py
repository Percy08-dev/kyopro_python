def main():
    a, b, x = map(int, input().split())
    
    if x-a < b and x-a >= 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()