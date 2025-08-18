# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(curr):
            if curr is None:
                return [True, 0]

            left = depth(curr.left)
            right = depth(curr.right)
            absol = abs(left[1]-right[1])
            balanced =  absol <= 1 and (left[0] and right[0] )
            
            return [balanced,1+ max(left[1], right[1])]
            
        if root is None:
            return True

        res = depth(root)

        return  res[0]
        
        