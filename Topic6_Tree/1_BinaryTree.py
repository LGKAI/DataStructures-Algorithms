class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if not root: return []
    result = []
    result += inorder(root.left)
    result.append(root.val)
    result += inorder(root.right)
    return result

def preorder(root):
    if not root: return []
    result = []
    result.append(root.val)
    result += preorder(root.left)
    result += preorder(root.right)
    return result

def postorder(root):
    if not root: return []
    result = []
    result += postorder(root.left)
    result += postorder(root.right)
    result.append(root.val)
    return result

def levelorder(root):
    if not root: return []
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

def build_tree(table):
    # Xây cây từ bảng dạng (index, value, left_index, right_index)
    nodes = {}
    for idx, val, _, _ in table:
        nodes[idx] = TreeNode(val)
    for idx, _, left, right in table:
        if left != -1:
            nodes[idx].left = nodes[left]
        if right != -1:
            nodes[idx].right = nodes[right]
    return nodes[0] # gốc là node 0

def evaluate(root, variables):
    if not root:
        return 0
    if root.val not in '+-*/':
        return variables[root.val]
    left = evaluate(root.left, variables)
    right = evaluate(root.right, variables)
    if root.val == '+': return left + right
    if root.val == '-': return left - right
    if root.val == '*': return left * right
    if root.val == '/': return left / right


if __name__ == "__main__":
    # Tạo một cây nhị phân để kiểm tra:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Inorder:", inorder(root))       # [4, 2, 5, 1, 3, 6]
    print("Preorder:", preorder(root))     # [1, 2, 4, 5, 3, 6]
    print("Postorder:", postorder(root))   # [4, 5, 2, 6, 3, 1]
    print("Levelorder:", levelorder(root)) # [1, 2, 3, 4, 5, 6]


    # Bảng biểu diễn cây nhị phân: (index, value, left_index, right_index)
    table = [
        (0, '*', 1, 2),
        (1, '-', 3, 4),
        (2, '/', 5, 6),
        (3, 'a', -1, -1),
        (4, 'b', -1, -1),
        (5, 'c', -1, -1),
        (6, 'd', -1, -1)
    ]
    # Giá trị biến
    variables = {
        'a': 10,
        'b': 4,
        'c': 12,
        'd': 3
    }
    root = build_tree(table)
    print("Inorder traversal:  ", inorder(root))     # ['a', '-', 'b', '*', 'c', '/', 'd']
    print("Preorder traversal: ", preorder(root))    # ['*', '-', 'a', 'b', '/', 'c', 'd']
    print("Postorder traversal:", postorder(root))   # ['a', 'b', '-', 'c', 'd', '/', '*']
    print("Levelorder traversal:", levelorder(root)) # ['*', '-', '/', 'a', 'b', 'c', 'd']
    # Tính biểu thức
    result = evaluate(root, variables)
    print("Giá trị biểu thức:", result) # (10 - 4) * (12 / 3) = 6 * 4 = 24