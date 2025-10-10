class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def new_node(data: int) -> Node:
    return Node(data)

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert_node(root: Node, data: int) -> Node:
    if not root:
        return new_node(data)
    elif data < root.key:
        root.left = insert_node(root.left, data)
    elif data > root.key:
        root.right = insert_node(root.right, data)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1 and data < root.left.key:
        return right_rotate(root)
    if balance < -1 and data > root.right.key:
        return left_rotate(root)
    if balance > 1 and data > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and data < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def search_node(root: Node, data: int) -> Node:
    if not root or root.key == data:
        return root
    elif data < root.key:
        return search_node(root.left, data)
    else:
        return search_node(root.right, data)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete_node(root: Node, data: int) -> Node:
    if not root:
        return root
    elif data < root.key:
        root.left = delete_node(root.left, data)
    elif data > root.key:
        root.right = delete_node(root.right, data)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def nlr(root: Node):
    if root:
        print(root.key, end=' ')
        nlr(root.left)
        nlr(root.right)

def lnr(root: Node):
    if root:
        lnr(root.left)
        print(root.key, end=' ')
        lnr(root.right)

def lrn(root: Node):
    if root:
        lrn(root.left)
        lrn(root.right)
        print(root.key, end=' ')

def level_order(root: Node):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.key, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    root = None
    values = [8, 6, 5, 7, 10, 9]
    for val in values:
        root = insert_node(root, val)

    print("Pre-order traversal:")
    nlr(root)
    print("\nIn-order traversal:")
    lnr(root)
    print("\nPost-order traversal:")
    lrn(root)

    root = delete_node(root, 8)
    print("\nLevel-order traversal after deleting 8:")
    level_order(root)