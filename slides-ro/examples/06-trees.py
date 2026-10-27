from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search(root, target):
    if root is None:
        return False
    if target == root.value:
        return True
    if target < root.value:
        return search(root.left, target)
    return search(root.right, target)


def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def min_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def remove(root, value):
    if root is None:
        return None
    if value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = min_node(root.right)
        root.value = successor.value
        root.right = remove(root.right, successor.value)
    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")


def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)


def bfs_levels(root):
    if root is None:
        return
    queue = deque([root])
    level = 0
    while queue:
        level_size = len(queue)
        print("Level", level, end=": ")
        for _ in range(level_size):
            current = queue.popleft()
            print(current.value, end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print()
        level += 1


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    print("Four-node binary tree:")
    print(root.left.left.value)
    print(root.right.left is None)

    bst = TreeNode(4)
    bst.left = TreeNode(2)
    bst.right = TreeNode(7)
    bst.left.left = TreeNode(1)
    bst.left.right = TreeNode(3)
    bst.right.left = TreeNode(6)
    bst.right.right = TreeNode(9)

    print("BST search:")
    print(search(bst, 6))
    print(search(bst, 5))
    print(search(None, 6))

    bst = insert(bst, 5)
    print("After insert 5:")
    print(search(bst, 5))

    bst = remove(bst, 3)
    bst = remove(bst, 6)
    bst = remove(bst, 4)
    print("After remove 3, 6, 4:")
    print(bst.value)
    print(search(bst, 3), search(bst, 6), search(bst, 4))

    bst = remove(bst, 99)
    print("Missing value and empty tree:")
    print(bst.value)
    print(remove(None, 5))

    bst = None
    for value in [4, 2, 7, 1, 3, 6, 9]:
        bst = insert(bst, value)

    print("Inorder:")
    inorder(bst)
    print()
    print("Preorder:")
    preorder(bst)
    print()
    print("Postorder:")
    postorder(bst)
    print()
    print("BFS:")
    bfs(bst)
    print()
    print("BFS by level:")
    bfs_levels(bst)
