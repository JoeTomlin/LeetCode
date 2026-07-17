# given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4

# Solution:
# 1. Inorder traversal of the tree will give us the nodes in ascending order.
# 2. We can use a stack to implement the inorder traversal.
# 3. We can use a counter to keep track of the number of nodes visited.
# 4. When the counter is equal to k, we return the node's value.

# Time complexity: O(n)
# Space complexity: O(n)

# Code:
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return -1