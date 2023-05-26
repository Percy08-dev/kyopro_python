def main():
    s = input()
    O = "oxxoxxoxxoxxoxxoxxoxxoxxoxx"

    ans = "No"

    for i in range(len(O) - len(s)):
        if O[i:i+len(s)] == s:
            ans = "Yes"
            break
    
    print(ans)


if __name__ == "__main__":
    main()