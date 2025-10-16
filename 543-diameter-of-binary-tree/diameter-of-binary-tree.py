# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #   stand at the root node, treat left and right branches of the tree as 2 seperate trees.
    #   get the maximum heights from both the trees add them, return as diameter
    #   watch striver vid for depth: Best explaination
        self.max_dia = 0
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            self.max_dia = max(self.max_dia, (left+right))
            return 1+max(left, right)

        dfs(root)

        return self.max_dia