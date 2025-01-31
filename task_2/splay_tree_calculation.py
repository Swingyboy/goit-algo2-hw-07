# Implementing Splay Tree Node
class SplayTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# Implementing Splay Tree for Fibonacci caching
class SplayTree:
    def __init__(self):
        self.root = None

    def _splay(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            if not root.left:
                return root
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._rotate_left(root.left)
            return self._rotate_right(root) if root.left else root

        else:
            if not root.right:
                return root
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._rotate_right(root.right)
            return self._rotate_left(root) if root.right else root

    def _rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        return right

    def _rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        return left

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root.value if self.root and self.root.key == key else None

    def insert(self, key, value):
        if not self.root:
            self.root = SplayTreeNode(key, value)
            return

        self.root = self._splay(self.root, key)
        if self.root.key == key:
            return

        new_node = SplayTreeNode(key, value)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

# Fibonacci with Splay Tree caching
def fibonacci_splay(n, tree):
    cached_value = tree.search(n)
    if cached_value is not None:
        return cached_value

    if n < 2:
        tree.insert(n, n)
        return n

    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result
