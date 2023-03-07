""" Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

________________

speed
O(N)
"""
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def checkChilds(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if (left is None and right is None):
            return True
        elif (left is None or right is None):
            return False

        if left.val == right.val:
            left_res = self.checkChilds(left.right, right.left)
            right_res = self.checkChilds(left.left, right.right)
            return left_res and right_res
        else: 
            return False
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.checkChilds(root.left, root.right)