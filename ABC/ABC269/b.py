def main():
    s = [input() for _i in range(10)]
    lt = None
    rb = None

    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if lt == None:
                    lt = (j+1, i+1)
                    rb = (j+1, i+1)
                else:
                    rb = (j+1, i+1)
    
    print(lt[1], rb[1])
    print(lt[0], rb[0])

if __name__ == "__main__":
    main()