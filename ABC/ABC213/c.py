h, w, n = map(int, input().split())

h_list = [0 for i in range(n)]
w_list = [0 for i in range(n)]

for i in range(n):
    h_list[i], w_list[i] = map(int, input().split())


h_dict = dict(zip(sorted(list(set(h_list))), range(n)))
w_dict = dict(zip(sorted(list(set(w_list))), range(n)))

for i in range(n):
    print(h_dict[h_list[i]] + 1, w_dict[w_list[i]] + 1)