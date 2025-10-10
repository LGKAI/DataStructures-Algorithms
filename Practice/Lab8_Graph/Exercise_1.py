def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        graph = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            graph.append(row)
    return graph

def dijkstra(graph, src):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n
    visited = [False] * n
    dist[src] = 0
    for _ in range(n):
        # Find the unvisited vertex with the smallest distance
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        # Update the distances to neighbors
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    prev[v] = u
    return dist, prev

def construct_path(prev, target):
    path = []
    while target is not None:
        path.insert(0, target)
        target = prev[target]
    return path

def main():
    graph = read_graph('graph.txt')
    src = int(input("Enter source vertex: "))
    dist, prev = dijkstra(graph, src)
    for dest in range(len(graph)):
        if dest == src:
            continue
        path = construct_path(prev, dest)
        if dist[dest] == float('inf'):
            print(f"No path from {src} to {dest}")
        else:
            print(f"The shortest path from {src} to {dest}: {' -> '.join(map(str, path))}.")


if __name__ == "__main__":
    main()