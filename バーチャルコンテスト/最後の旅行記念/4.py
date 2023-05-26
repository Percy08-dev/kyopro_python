def main():
    s = input()
    print(s + "s" if s[-1] != "s" else s + "es")

if __name__ == "__main__":
    main()