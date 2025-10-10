class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

# Exercise 1
def new_node(data: int) -> Node:
    return Node(data)

def insert(root: Node, data: int) -> Node:
    if root is None:
        return new_node(data)
    if data < root.key:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def search(root: Node, data: int) -> Node:
    if root is None or root.key == data:
        return root
    if data < root.key:
        return search(root.left, data)
    return search(root.right, data)

def delete(root: Node, data: int) -> Node:
    if root is None:
        return root
    if data < root.key:
        root.left = delete(root.left, data)
    elif data > root.key:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        successor = root.right
        while successor.left:
            successor = successor.left
        root.key = successor.key
        root.right = delete(root.right, successor.key)
    return root

def preorder(root: Node) -> None:
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root: Node) -> None:
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def postorder(root: Node) -> None:
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')

def level_order(root: Node) -> None:
    if root is None:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.key, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Exercise 2
def height(root: Node) -> int:
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))

def count_nodes(root: Node) -> int:
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def sum_nodes(root: Node) -> int:
    if root is None:
        return 0
    return root.key + sum_nodes(root.left) + sum_nodes(root.right)

def count_leaves(root: Node) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

def count_less(root: Node, x: int) -> int:
    if root is None:
        return 0
    if root.key < x:
        return 1 + count_less(root.left, x) + count_less(root.right, x)
    else:
        return count_less(root.left, x)

def count_greater(root: Node, x: int) -> int:
    if root is None:
        return 0
    if root.key > x:
        return 1 + count_greater(root.left, x) + count_greater(root.right, x)
    else:
        return count_greater(root.right, x)


if __name__ == "__main__":
    root = None
    for v in [8, 6, 5, 7, 10, 9]:
        root = insert(root, v)

    print("Pre-order:")
    preorder(root)
    print("\n")
    
    print("In-order:")
    inorder(root)
    print("\n")

    print("Post-order:")
    postorder(root)
    print("\n")

    root = delete(root, 8)
    print("Level-order sau khi xoá node 8:")
    level_order(root)

    x = 7
    print(f"\nChiều cao cây: {height(root)}")
    print(f"Tổng số node: {count_nodes(root)}")
    print(f"Tổng giá trị các node: {sum_nodes(root)}")
    print(f"Số lá: {count_leaves(root)}")
    print(f"Số node < {x}: {count_less(root, x)}")
    print(f"Số node > {x}: {count_greater(root, x)}")
