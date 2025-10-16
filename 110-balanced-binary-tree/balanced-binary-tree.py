# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_diff = False
        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            diff = abs(left-right)
            if diff > 1:
                self.max_diff = True
            return 1+max(left, right)

        dfs(root)
        if self.max_diff:
            return False
        else:
            return True

