# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:  # If list is empty, no tree
            return None
        
        mid = len(nums) // 2  # Pick middle element
        root = TreeNode(nums[mid])  # Make it the root
        
        # Build subtrees
        root.left = self.sortedArrayToBST(nums[:mid])      # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])   # Right half
        
        return root
