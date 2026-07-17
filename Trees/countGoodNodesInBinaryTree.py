# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.goodNodesHelper(root, root.val)

    def goodNodesHelper(self, root: TreeNode, max_val: int) -> int:
        if not root:
            return 0
        count = 0
        if root.val >= max_val:
            count += 1
        count += self.goodNodesHelper(root.left, max(max_val, root.val))
        count += self.goodNodesHelper(root.right, max(max_val, root.val))
        return count
    
    def countGoodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.goodNodesHelper(root, root.val)