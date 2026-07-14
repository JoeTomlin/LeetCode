# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# The tree is guaranteed to have at least one node.
# The tree is guaranteed to have at most 1000 nodes.
# The tree is guaranteed to have unique values.
# The tree is guaranteed to have at most one lowest common ancestor for any two nodes.
# The tree is guaranteed to have at most one lowest common ancestor for any two nodes. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case
        if not root:
            return []
        result = []
        # initialize the queue
        queue = deque([root])
        # while the queue is not empty
        while queue:
            # get the level size
            level_size = len(queue)
            # initialize the level list
            level = []
            # iterate through the level size
            for _ in range(level_size):
                current = queue.popleft()
                level.append(current.val)
                # add the left and right children to the queue
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            # add the level list to the result 
            result.append(level)
        return result

# O(n) time complexity
# O(n) space complexity