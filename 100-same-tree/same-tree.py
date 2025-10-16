# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            def dfs_pq(p, q):
                if p is None and q is not None:
                    return False
                if p is not None and q is None:
                    return False
                if p is None and q is None:
                    return True
                if p and q and p.val == q.val:
                    return (dfs_pq(p.left, q.left) and dfs_pq(p.right, q.right))         
                return False
            return dfs_pq(p,q)
                

                
                