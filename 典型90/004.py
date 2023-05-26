import numpy as np
import sys
input = sys.stdin.buffer.readline

h, w = map(int, input().split())
array = np.array([input().split() for _ in range(h)], dtype=np.int64)
h_sum = np.sum(array, axis=0)
v_sum = np.sum(array, axis=1)
res = np.add.outer(v_sum, h_sum) - array
for a in res.tolist():
    print(*a)