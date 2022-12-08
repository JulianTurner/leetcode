# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getLeaf(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return self.getLeaf(root.left) + self.getLeaf(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # get leafs from root1
        leafs1 = self.getLeaf(root1)
        # get leafs from root2
        leafs2 = self.getLeaf(root2)
               
        # check if the leafs match content
        if leafs1 == leafs2:
        # return true if they match
            return True
        else:
            return False


print(leafSimilar([3,5,1,6,2,9,8,null,null,7,4],[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]))
