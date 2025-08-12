# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = None
        
        def dfs(root):
            if root is None:
                return 
            dfs(root.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = root.val
            dfs(root.right)
            return 
        dfs(root)
        return  self.res

        