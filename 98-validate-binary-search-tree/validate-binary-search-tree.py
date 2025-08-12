# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        
        def dfs_valid (root):
            if not root:
                return True

            a = dfs_valid(root.left)
            if self.prev is not None and self.prev >= root.val:
                print(self.prev, root.val)
                return False
            self.prev = root.val
            b = dfs_valid(root.right)

            return a and b

        return dfs_valid(root)
        """          if root is None:
                return True
            if (left < root.val < right) is False:# preorder processing
                return False
            
            left_flag = dfs_Valid(root.left, left, root.val)  # traverse to left 
            right_flag = dfs_Valid(root.right, root.val, right) # traverse to right
            return left_flag and right_flag

        return dfs_Valid(root, float('-inf'), float('+inf'))
        """


        
        