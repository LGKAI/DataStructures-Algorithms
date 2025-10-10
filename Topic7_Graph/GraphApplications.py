from collections import deque
import heapq

# Sắp xếp topo bằng Kahn's Algorithm (BFS)
def topo_sort_kahn(graph, n):
    indegree = [0] * n
    for u in range(n):
        for v in graph[u]:
            indegree[v] += 1
    queue = deque([u for u in range(n) if indegree[u] == 0])
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    if len(result) != n:
        print("Có chu trình! (Kahn)")
    else:
        print("Thứ tự topo (Kahn):", result)

# Giải thuật khác: Sắp xếp topo bằng DFS
def topo_sort_dfs(graph, n):
    visited = [False] * n
    result = []

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        result.append(u)

    for u in range(n):
        if not visited[u]:
            dfs(u)
    result.reverse()
    print("Thứ tự topo (DFS):", result)

# Tìm cây khung nhỏ nhất bằng Prim's Algorithm
def prim(graph, n):
    visited = [False] * n
    min_heap = [(0, 0)] # (trọng số, đỉnh)
    total_weight = 0
    mst_edges = []
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        mst_edges.append((u, weight))
        for v, w in graph.get(u, []):
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    print("Cây khung tối tiểu có tổng trọng số:", total_weight)
    print("Cạnh trong MST:", mst_edges)

# Tìm đường đi ngắn nhất bằng Dijkstra's Algorithm
def dijkstra(graph, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    heap = [(0, start)] # (khoảng cách, đỉnh)
    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]: continue
        visited[u] = True
        for v, w in graph.get(u, []):
            if not visited[v] and dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    print(f"Khoảng cách ngắn nhất từ đỉnh {start}:")
    for i in range(n):
        print(f"Đỉnh {i}: {dist[i]}")
    return dist

if __name__ == '__main__':
    pass