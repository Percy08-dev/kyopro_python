import networkx as nx

def f(G, v):
    res = [v]
    x = list(G[v].keys())

    while len(x) != 0:
        k = x.pop()



def main():
    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    vertex = [tuple(sorted(map(int, input().split()))) for _ in range(n-1)]
    query = [tuple(map(int, input().split())) for _ in range(q)]

    G = nx.DiGraph()
    G.add_edges_from(vertex)

    print(G.nodes)
    # for (v, k) in query:
    #    nums = 




if __name__ == "__main__":
    main()