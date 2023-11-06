# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, strnum):
            if not node:
                return 0
            strnum += str(node.val)
            if not node.left and not node.right:
                return int(strnum)
            return dfs(node.left, strnum) + dfs(node.right, strnum)
        return dfs(root, "")
