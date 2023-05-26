import collections
s = [input() for _ in range(3)]

m = ["ABC" , "ARC" , "AGC" , "AHC"]

print([key for key, volue in collections.Counter(s + m).items() if volue == 1][0])