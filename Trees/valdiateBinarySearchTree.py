# given the root of a binary tree, determine if it is a valid binary search tree (BST).

# assume a BST is defined as follows:
# the left subtree of a node contains only nodes with keys less than the node's key.
# the right subtree of a node contains only nodes with keys greater than the node's key.
# both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))

    def isValidBSTHelper(self, root: TreeNode, min_val: int, max_val: int) -> bool:
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.isValidBSTHelper(root.left, min_val, root.val) and self.isValidBSTHelper(root.right, root.val, max_val)