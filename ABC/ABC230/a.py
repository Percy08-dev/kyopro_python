def main():
    n = int(input())
    if n >= 42:
        n += 1
    
    print("AGC{}".format(str(n).zfill(3)))

if __name__ == "__main__":
    main()