# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if (p is None and q is not None ) or (q is None and p is not None ): # check for either of them, if one of them is true
                return False
            elif p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            return False
            """
            p_arr, q_arr = [], []

            def dfs(root, arr):

                if root is None:
                    return 

                dfs(root.left, arr)
                arr.append(root.left.val if root.left else None)
                arr.append(root.val)     
                arr.append(root.right.val if root.right else None)
                                             
                dfs(root.right, arr)

            dfs(p, p_arr)
            dfs(q, q_arr)
            
            print(p_arr)
            print(q_arr)

            return True if p_arr == q_arr else False"""
                

            
