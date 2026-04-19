# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _postorderTraversal(self, ans: List[TreeNode], node: Optional[TreeNode]):
        if not node:
            return
        
        self._postorderTraversal(ans, node.left)
        self._postorderTraversal(ans, node.right)

        ans.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self._postorderTraversal(ans, root)
        return ans