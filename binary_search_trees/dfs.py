# A deapth-first search (DFS) is a way to traverse a tree or graph.
# It starts at the root node and explores as far as possible along each branch
# before backtracking.

class TreeNode:

    def __init__(self, key, value=None, left=None, right=None):
        if not value:
            value = key
        self.key = key
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode {self.val}"


class Tree:

    def __init__(self):
        self.root = None

    def inorder_helper(self, current_node, results):
        if not current_node:
            return results

        self.inorder_helper(current_node.left, results)
        results.append({
            "key": current_node.key,
            "value": current_node.val
        })
        self.inorder_helper(current_node.right, results)
        return results
    
    def inorder(self):
        results = []
        return self.inorder_helper(self.root, results)

    def preorder_helper(self, current_node, results):
        if not current_node:
            return results

        results.append({
            "key": current_node.key,
            "value": current_node.val
        })
        self.preorder_helper(current_node.left, results)
        self.preorder_helper(current_node.right, results)
        
        return results

    def preorder(self):
        results = []
        return self.preorder_helper(self.root, results)

    def postorder_helper(self, current_node, results):
        if not current_node:
            return results

        self.postorder_helper(current_node.left, results)
        self.postorder_helper(current_node.right, results)
        results.append({
            "key": current_node.key,
            "value": current_node.val
        })
        
        return results
    
    def postorder(self):
        results = []
        return self.postorder_helper(self.root, results)