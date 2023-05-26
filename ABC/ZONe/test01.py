import time

x = [i for i in range(10**8 * 3)]
t1 = time.perf_counter()
x = x[::-1]
t2 = time.perf_counter()
print(t2 - t1)

t1 = time.perf_counter()
x = reversed(x)
t2 = time.perf_counter()
print( t2 - t1)

# スライス[::-1]
# 20.1439417
# revesed
# 0.0007535999999959131
# 圧倒的にreverseのほうが速い