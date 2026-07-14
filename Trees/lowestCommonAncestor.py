# Given a binary tree, find the lowest common ancestor of two given nodes in the tree.
# The lowest common ancestor is the deepest node that has both nodes as descendants.
# The tree is guaranteed to have unique values.
# The tree is guaranteed to have at least two nodes.
# The tree is guaranteed to have at most one lowest common ancestor for any two nodes.
# The tree is guaranteed to have at most one lowest common ancestor for any two nodes. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # edge case
        if not root:
            return None
        # if the root is the same as p or q, return the root    
        if root.val == p.val or root.val == q.val:
            return root
        # if the root is not the same as p or q, recurse on the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if the left and right subtrees are not None, return the root
        if left and right:
            return root
        # if the left or right subtree is not None, return the left or right subtree
        return left or right
