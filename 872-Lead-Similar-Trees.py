# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Generator to yield all leafs in a tree
    def leafs(self, root):
        if root:
            # Check if the node is a leaf
            if root.left is None and root.right is None:
                yield root.val
            # If not a leaf, check the left and right nodes
            for node in self.leafs(root.left):
                yield node
            for node in self.leafs(root.right):
                yield node

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Create Generator expressions for both trees
        root1Generator = (node for node in self.leafs(root1))
        root2Generator = (node for node in self.leafs(root2))
        # Compare the two generators
        while True:
            if next(root1Generator) != next(root2Generator):
                return False
            else:
                return True

