# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def traverse(node):
            if not node:
                return 
            
            ans = traverse(node.left)
            if ans is not None:
                return ans

            self.count += 1
            if self.count == k:
                return node.val

            ans = traverse(node.right)
            if ans is not None:
                return ans
            
        ans = traverse(root)
        return ans