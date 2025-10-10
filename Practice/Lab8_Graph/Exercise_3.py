def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        graph = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            graph.append(row)
    return graph

def prim(graph):
    n = len(graph)
    selected = [False] * n
    edge_list = []
    # Start from vertex 0
    selected[0] = True
    for _ in range(n - 1):
        min_weight = float('inf')
        u = -1
        v = -1
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0 and graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        u, v = i, j
        if u != -1 and v != -1:
            edge_list.append((u, v, min_weight))
            selected[v] = True
    return edge_list

def main():
    graph = read_graph('graph.txt')
    mst_edges = prim(graph)
    print("Edge\tWeight")
    for u, v, weight in mst_edges:
        print(f"{u} - {v}\t{weight}")


if __name__ == "__main__":
    main()