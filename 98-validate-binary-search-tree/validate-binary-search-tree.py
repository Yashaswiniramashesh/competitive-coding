# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Valid (root, left, right):
            if root is None:
                return True
            if (left < root.val < right) is False:
                return False
            
            left_flag = Valid(root.left, left, root.val) 
            right_flag = Valid(root.right, root.val, right)
            return left_flag and right_flag

        return Valid(root, float('-inf'), float('+inf'))
                
        