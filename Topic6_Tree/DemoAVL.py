class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    x.height = max(get_height(x.left), get_height(x.right)) + 1
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(get_height(x.left), get_height(x.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    return y

def insert(node, key):
    if not node:
        return AVLNode(key)
    if key < node.val:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)
    if balance > 1 and key < node.left.val:
        return right_rotate(node)
    if balance < -1 and key > node.right.val:
        return left_rotate(node)
    if balance > 1 and key > node.left.val:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and key < node.right.val:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    return node

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def find_lca(root, p, q):
    if not root:
        return None
    if root.val > p and root.val > q:
        return find_lca(root.left, p, q)
    if root.val < p and root.val < q:
        return find_lca(root.right, p, q)
    return root

def distance_from_node(root, val):
    if root.val == val:
        return 0
    elif val < root.val:
        return 1 + distance_from_node(root.left, val)
    else:
        return 1 + distance_from_node(root.right, val)
    
def find_distance(root, p, q):
    lca = find_lca(root, p, q)
    return distance_from_node(lca, p) + distance_from_node(lca, q)

if __name__ == '__main__':
    n = int(input()) # 7
    elements = list(map(int, input().split())) # 7 3 9 2 5 4 8
    p, q = map(int, input().split()) # 2 4

    root = None
    for num in elements:
        root = insert(root, num)

    print(' '.join(map(str, level_order_traversal(root)))) # 5 3 8 2 4 7 9
    print(find_distance(root, p, q)) # 2