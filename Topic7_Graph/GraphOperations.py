from collections import deque

class GraphMatrix:
    def __init__(self, size): # khởi tạo ma trận kề với size x size phần tử 0
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, u, v): # thêm cạnh (vô hướng)
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def remove_edge(self, u, v): # xóa cạnh (vô hướng)
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def is_edge(self, u, v): # kiểm tra xem có cạnh không
        return self.matrix[u][v] == 1

    def num_vertices(self): # đếm số đỉnh
        return self.size

    def num_edges(self): # đếm số cạnh (chia 2 vì mỗi cạnh đếm 2 lần)
        return sum(sum(row) for row in self.matrix) // 2

    def __str__(self):
        return "\n".join(str(row) for row in self.matrix)

    def dfs(self, start, visited=None): # phiên bản đệ quy
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for v in range(self.size):
            if self.matrix[start][v] == 1 and v not in visited:
                self.dfs(v, visited)

    def dfs_iterative(self, start): # phiên bản không đệ quy
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                for v in range(self.size - 1, -1, -1):
                    if self.matrix[node][v] == 1 and v not in visited:
                        stack.append(v)

    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        while queue:
            u = queue.popleft()
            print(u, end=' ')
            for v in range(self.size):
                if self.matrix[u][v] == 1 and v not in visited:
                    visited.add(v)
                    queue.append(v)

    def connected_components(self): # tìm các thành phần liên thông
        visited = set()
        components = []
        for v in range(self.size):
            if v not in visited:
                comp = []
                self._dfs_collect(v, visited, comp)
                components.append(comp)
        return components

    def _dfs_collect(self, v, visited, comp):
        visited.add(v)
        comp.append(v)
        for u in range(self.size):
            if self.matrix[v][u] == 1 and u not in visited:
                self._dfs_collect(u, visited, comp)


class GraphList:
    def __init__(self): # khởi tạo danh sách kề (dictionary)
        self.adj_list = {}

    def add_edge(self, u, v): # thêm cạnh
        self.adj_list.setdefault(u, []).append(v)
        self.adj_list.setdefault(v, []).append(u)

    def remove_edge(self, u, v): # xóa cạnh
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def is_edge(self, u, v): # kiểm tra cạnh
        return v in self.adj_list.get(u, [])

    def num_vertices(self): # đếm số đỉnh
        return len(self.adj_list)

    def num_edges(self): # đếm số cạnh
        return sum(len(neigh) for neigh in self.adj_list.values()) // 2

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.adj_list.items())

    def dfs(self, start, visited=None): # phiên bản đệ quy
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def dfs_iterative(self, start): # phiên bản không đệ quy
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)

    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        while queue:
            u = queue.popleft()
            print(u, end=' ')
            for neighbor in self.adj_list.get(u, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def connected_components(self): # tìm các thành phần liên thông
        visited = set()
        components = []
        for v in self.adj_list.keys():
            if v not in visited:
                comp = []
                self._dfs_collect(v, visited, comp)
                components.append(comp)
        return components

    def _dfs_collect(self, v, visited, comp):
        visited.add(v)
        comp.append(v)
        for u in self.adj_list.get(v, []):
            if u not in visited:
                self._dfs_collect(u, visited, comp)


# Chuyển từ ma trận kề sang danh sách kề
def matrix_to_list(matrix):
    g_list = GraphList()
    size = len(matrix)
    for u in range(size):
        for v in range(u, size):
            if matrix[u][v] == 1:
                g_list.add_edge(u, v)
    return g_list

# Chuyển từ danh sách kề sang ma trận kề
def list_to_matrix(adj_list):
    size = max(adj_list.adj_list.keys()) + 1
    g_matrix = GraphMatrix(size)
    for u, neighbors in adj_list.adj_list.items():
        for v in neighbors:
            g_matrix.add_edge(u, v)
    return g_matrix


if __name__ == '__main__':
    print("Graph with Adjacency Matrix")
    g_matrix = GraphMatrix(4)
    g_matrix.add_edge(0, 1)
    g_matrix.add_edge(0, 2)
    g_matrix.add_edge(1, 3)
    print(g_matrix)
    print(f"Vertices: {g_matrix.num_vertices()}, Edges: {g_matrix.num_edges()}")
    print(f"Edge 0-2? {g_matrix.is_edge(0,2)}")
    print("DFS from 0:", end=' ')
    g_matrix.dfs(0)
    print("\nBFS from 0:", end=' ')
    g_matrix.bfs(0)
    print("\nConnected Components:", g_matrix.connected_components(), "\n")

    print("Convert Matrix to List")
    g_list = matrix_to_list(g_matrix.matrix)
    print(g_list)
    print(f"Vertices: {g_list.num_vertices()}, Edges: {g_list.num_edges()}")
    print("DFS from 0:", end=' ')
    g_list.dfs(0)
    print("\nBFS from 0:", end=' ')
    g_list.bfs(0)
    print("\nConnected Components:", g_list.connected_components(), "\n")

    print("Graph with Adjacency List")
    g_list2 = GraphList()
    g_list2.add_edge(0, 1)
    g_list2.add_edge(1, 2)
    g_list2.add_edge(2, 3)
    g_list2.add_edge(4, 5) # thêm 1 thành phần liên thông khác
    print(g_list2)
    print(f"Vertices: {g_list2.num_vertices()}, Edges: {g_list2.num_edges()}")
    print(f"Edge 1-3? {g_list2.is_edge(1,3)}")
    print("DFS from 0:", end=' ')
    g_list2.dfs(0)
    print("\nBFS from 0:", end=' ')
    g_list2.bfs(0)
    print("\nConnected Components:", g_list2.connected_components())