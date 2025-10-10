class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

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
        # Trường hợp chỉ có 1 hoặc không có con
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Trường hợp có 2 con: tìm node nhỏ nhất bên phải
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


if __name__ == '__main__':
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]

    for v in values:
        root = insert(root, v)

    print("In-order traversal:")
    inorder(root) # 20 30 40 50 60 70 80
    print("\n")

    print("Pre-order traversal:")
    preorder(root) # 50 30 20 40 70 60 80
    print("\n")

    print("Post-order traversal:")
    postorder(root) # 20 40 30 60 80 70 50
    print("\n")

    print("Level-order traversal:")
    level_order(root) # 50 30 70 20 40 60 80
    print("\n")

    print("Tìm node có giá trị 60:", end = " ")
    result = search(root, 60)
    print("Tìm thấy" if result else "Không tìm thấy")
    print()

    print("Xoá node có giá trị 70 và duyệt lại In-order:")
    root = delete(root, 70)
    inorder(root)  # 20 30 40 50 60 80

