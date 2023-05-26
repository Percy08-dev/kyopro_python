def main():
    N, M, X, T, D = map(int, input().split()) 
    
    keika = min(X, X - M) if X -M > 0 else 0
    
    print(T - keika * D)


if __name__ == "__main__":
    main()
