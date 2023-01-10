# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


sol = Solution()
ex_1 = ([1,2,3], [1,2,3], True) # expected True
ex_2 = ([1,2], [1,None,2], False) # expected False
ex_3 = ([1,2,1], [1,1,2], False) # expected False

examples = [ex_1, ex_2, ex_3]
for (p_ex, q_ex, expected_ex) in examples:
    result = sol.isSameTree(p_ex, q_ex)
    assert expected_ex == result,\
        f"expected {expected_ex} but got {result} for input p={p_ex} q_ex={q_ex}"

print("All tests passed!")
