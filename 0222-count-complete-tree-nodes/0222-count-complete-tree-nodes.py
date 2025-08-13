# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        # Function to get the depth of leftmost path
        def leftDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        
        # Function to get the depth of rightmost path
        def rightDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.right
            return depth
        
        left = leftDepth(root)
        right = rightDepth(root)
        
        # If left depth == right depth, tree is perfect
        if left == right:
            return (1 << left) - 1  # 2^depth - 1
        
        # Otherwise count recursively
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
