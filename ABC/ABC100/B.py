d, n = map(int, input().split())
print(100**d*n if n != 100 else 100**d*(n+1))

#n = 100の時、d+1回100で割ることができるから