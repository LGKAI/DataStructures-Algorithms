def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        edges = []
        for i in range(n):
            row = list(map(int, f.readline().split()))
            for j in range(i + 1, n): # avoid duplicates in undirected graph
                if row[j] != 0:
                    edges.append((row[j], i, j)) # (weight, u, v)
    return n, edges

def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot == yroot:
        return False # already connected
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
    return True

def kruskal(n, edges):
    mst = []
    edges.sort() # sort edges by weight
    parent = list(range(n))
    rank = [0] * n
    for weight, u, v in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
        if len(mst) == n - 1:
            break
    return mst

def main():
    n, edges = read_graph('graph.txt')
    mst_edges = kruskal(n, edges)
    print("Edge\tWeight")
    for u, v, weight in mst_edges:
        print(f"{u} - {v}\t{weight}")


if __name__ == "__main__":
    main()