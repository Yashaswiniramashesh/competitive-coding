# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ele_arr = []
        
        def dfs_valid (root):
            if not root:
                return
            dfs_valid(root.left)
            ele_arr.append(root.val)
            dfs_valid(root.right)
            return 

        dfs_valid(root)
        print(ele_arr)
        for i in range(1, len(ele_arr)):
            if ele_arr[i-1] >= ele_arr[i]:
                return False
        return True
        """          if root is None:
                return True
            if (left < root.val < right) is False:# preorder processing
                return False
            
            left_flag = dfs_Valid(root.left, left, root.val)  # traverse to left 
            right_flag = dfs_Valid(root.right, root.val, right) # traverse to right
            return left_flag and right_flag

        return dfs_Valid(root, float('-inf'), float('+inf'))
        """


        
        