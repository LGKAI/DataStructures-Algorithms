def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        graph = []
        for i in range(n):
            row = list(map(int, f.readline().split()))
            for j in range(n):
                if row[j] != 0:
                    graph.append((i, j, row[j])) # (u, v, weight)
    return n, graph

def bellman_ford(n, edges, src):
    dist = [float('inf')] * n
    prev = [None] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
    # Check for negative-weight cycles (not expected here)
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Graph contains a negative-weight cycle.")
            return None, None
    return dist, prev

def construct_path(prev, target):
    path = []
    while target is not None:
        path.insert(0, target)
        target = prev[target]
    return path

def main():
    n, edges = read_graph('graph.txt')
    src = int(input("Enter source vertex: "))
    dist, prev = bellman_ford(n, edges, src)
    if dist is None:
        return
    for dest in range(n):
        if dest == src:
            continue
        path = construct_path(prev, dest)
        if dist[dest] == float('inf'):
            print(f"No path from {src} to {dest}")
        else:
            print(f"The shortest path from {src} to {dest}: {' -> '.join(map(str, path))}.")


if __name__ == "__main__":
    main()