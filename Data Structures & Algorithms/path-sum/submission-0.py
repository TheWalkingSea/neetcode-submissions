# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _hasPathSum(self, currSum: int, curr: Optional[TreeNode], targetSum: int) -> bool:
        if (curr is None):
            return False
        currSum += curr.val

        if (not curr.left and not curr.right and currSum == targetSum):
            return True

        return self._hasPathSum(currSum, curr.left, targetSum) or self._hasPathSum(currSum, curr.right, targetSum)



    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self._hasPathSum(0, root, targetSum)
        