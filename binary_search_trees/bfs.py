# Breadth First Search
# Time Complexity: O(n)
# Breadth First Search is a tree traversal algorithm that starts at the root
# node and explores all of the neighboring nodes. It then explores all of the
# neighbor's neighbors and so on. It does this until it has explored all of the
# nodes in the tree.
# import deque from collections
# create a queue
# deque is used to create a queue because it is more efficient than a list
from collections import deque

class TreeNode:
    # This is the same TreeNode class from binary_search_trees/dfs.py
    def __init__(self, key, value=None, left=None, right=None):
        if not value:
            value = key
        self.key = key
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode {self.val}"

# Tree class with a breadth first search method
class Tree:
    def __init__(self):
        self.root = None

    def bfs(self):
        if self.root is None:
            return

        queue = deque([self.root])
        visited = [self.root.val]

        while queue:
            current_node = queue.popleft()

            if current_node.left is not None:
                visited.append(current_node.left.val)
                queue.append(current_node.left)

            if current_node.right is not None:
                visited.append(current_node.right.val)
                queue.append(current_node.right)

        return visited
