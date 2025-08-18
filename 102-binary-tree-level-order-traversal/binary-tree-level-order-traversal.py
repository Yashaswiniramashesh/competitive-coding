
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()

        q.append(root)

        while q:
            level = []
            q_len = len(q)
            for i in range(q_len):
                ele = q.popleft()
                
                if ele:
                    level.append(ele.val)
                    if ele.left is not None:
                        q.append(ele.left)
                    if ele.right is not None:
                        q.append(ele.right)
            if len(level) > 0:
                res.append(level)
            
        return res
            


